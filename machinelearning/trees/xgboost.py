
import numpy as np

from test.trees.treeRegression import Tree, treeNode


class TreeBase(Tree):
    def __init__(self, min_leafs=4, max_depth=20, max_bins=10):
        super(TreeBase, self).__init__()
        self.min_leafs = min_leafs
        self.max_depth = max_depth
        self.max_bins = max_bins
        self.lmds = 0.4
        self.gama = 0.5

    def splitdata(self, data, label, feature, value):
        left_condtion = data[:, feature] <= value
        left_d = data[left_condtion, :]
        right_d = data[~left_condtion, :]
        left_l = label[left_condtion, :]
        right_l = label[~left_condtion, :]
        return left_d, right_d, left_l, right_l

    def regleaf(self, label, epis=3):
        g = label[:, 0]
        h = label[:, 1]
        w = - np.sum(g) / (np.sum(h) + self.lmds)
        return np.round(w, epis)

    def regerr(self, label):
        g = label[:, 0]
        h = label[:, 1]
        fenzi = np.power(np.sum(g), 2)
        fenmu = np.sum(h) + self.lmds
        return np.round(fenzi / fenmu, 3)

    def createTree(self, data, label, depth=0):
        if np.array(label).shape[1] != 2:
            raise ValueError
        retTree = treeNode()

        if data.shape[0] < self.min_leafs:
            retTree.label_class = self.regleaf(data)
            return retTree

        # 可以添加其他条件,终止树 停止生长，分类和回归树有不同的搞法。
        # 这里阐释了如何 利用递归的思想去 建立决策树
        feat, val = self.choosebestsplit(data, label)
        # 如果没有可以再次切分的  feature 就返回val
        if feat is None or depth > self.max_depth:
            retTree.label_class = self.regleaf(label)
            return retTree

        # 这里先寻找切分点，然后再切分数据，会好点的
        retTree.feature = feat
        retTree.value = val
        lset, rset, llabel, rlabel = self.splitdata(data, label, feat, val)

        retTree.left_tree = self.createTree(lset, llabel, depth=depth + 1)
        retTree.right_tree = self.createTree(rset, rlabel, depth=depth + 1)
        return retTree

    def choosebestsplit(self, data, label):
        data = np.array(data)
        m, n = data.shape

        # 计算初始的方差。
        S = self.regerr(label)
        best_s = -np.inf
        best_feat = None
        best_val = None

        for i in range(n):  # n feature
            # 这么做的好处是 可以加快运行速度，其次可以减少偏态数据的影响，亲测可行
            # ，改善预测效果（方差小偏琦大的问题）
            minx = np.min(data[:, i])
            maxs = np.max(data[:, i])
            step = (maxs - minx) / self.max_bins
            # 可以采用直方图，百分位数据 进行数据切分， 每个切分的值一样对，这里的是艰巨一样。 3种方法。
            value_set = [minx + i * step for i in range(1, self.max_bins)]
            for j in value_set:
                mat0, mat1, llabel, rlabel = self.splitdata(data, label, i, j)
                #这里就是 xgboost的 划分依据,选择 改变最大的值。
                new_s = 0.5 * (self.regerr(llabel) + self.regerr(rlabel) - S) - self.gama
                if new_s > best_s:
                    best_feat = i
                    best_val = j
                    best_s = new_s
        # 当方差改善不明显时，则停止，没必要进行更新。
        return best_feat, best_val


class XgboostTree:
    """
    解决 二分类问题。
    """
    def __init__(self,
                 n_trees=100,
                 max_depth=10,
                 verbose=True):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.verbose = verbose
        self.lmds = 0.4
        self.gama = 0.5

    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-2 * x))

    def predict_line(self, model, line):
        if model.label_class is not None:
            return model.label_class, model
        split_feature = model.feature
        split_value = model.value
        if line[split_feature] > split_value:
            return self.predict_line(model.right_tree, line)
        else:
            return self.predict_line(model.left_tree, line)

    def __get_gama(self, data, mytree, target):
        last = {}
        for index, line in enumerate(data):
            temp_label, temp_node = self.predict_line(mytree, line)
            last.setdefault(temp_node, {})
            last[temp_node].setdefault("index", []).append(index)

            last[temp_node]['fm'] = temp_label
            last[temp_node].setdefault("label", []).append(target[index])

        loss = 0
        T = len(last.keys())
        # 每个样本 对应的 gama值，每个node 下的样本的gama值一样， 用于train, ml=>gama_list
        ml = {}
        # 每个node 的gama值，用于预测时
        new_last = {}
        for key, value in last.items():
            label = np.array(value["label"])
            loss += np.sum(label[:, 0]) / (np.sum(label[:, 1]) + self.lmds)

            index_list = value['index']
            gama = value['fm']
            new_last.setdefault(key, gama)
            for idx in index_list:
                ml.setdefault(idx, gama)
        gama_list = np.array([[int(i[0]), i[1]] for i in sorted(ml.items(), key=lambda row: row[0])])
        loss = -0.5 * loss + T * self.gama
        return gama_list, new_last, loss

    def fit(self, data, target):
        m, n = data.shape

        if len(target.shape) != 2:
            target = target.reshape(m, 1)
        # 初始化某些值
        f0 = 0.5 * np.log((1 + np.mean(target)) / (1 - np.mean(target)))
        fx = np.repeat(f0, m).reshape((m, 1))

        pred_dict = {}
        pred_dict.setdefault("init_fx", f0)

        for i in range(self.n_trees):
            dety = 2 * target / (1 + np.exp(2 * np.multiply(target, fx)))
            # 损失函数的 二阶倒数
            h = np.multiply(-2 * target / (1 + np.exp(-2 * np.multiply(target, fx))), dety)

            label = np.concatenate([dety, h], axis=1)
            mymodel = TreeBase(min_leafs=3, max_depth=self.max_depth)
            mytree = mymodel.createTree(data, label)

            # print("carttree deep is {}".format(mymodel.get_deep(mytree)))
            gama_list, node_gama, loss = self.__get_gama(data, mytree, target=label)
            if self.verbose:
                print("loss at {} is {}".format(i, loss))
            fx = fx + gama_list[:, 1:2]
            # 存储模型的参数
            pred_dict.setdefault("tree", []).append(mytree)
            pred_dict.setdefault("local_gama", []).append(node_gama)
        self.gdbt_modelparamter = pred_dict
        return self

    def gbdt_predict_line(self, line, bino=False):
        init_f0 = self.gdbt_modelparamter['init_fx']
        tree_list = self.gdbt_modelparamter['tree']
        local_gama_list = self.gdbt_modelparamter['local_gama']

        for tree, local_gama in zip(tree_list, local_gama_list):
            temp_pred, node = self.predict_line(tree, line)
            gama = local_gama[node]
            init_f0 += gama
        if bino:
            last_pred = 1 if self.__sigmoid(-init_f0) > self.__sigmoid(init_f0) else -1
            return last_pred
        else:
            return init_f0

    def gbdt_predict(self, data, bino=False):
        predicts = []
        for line in data:
            temp_pred = self.gbdt_predict_line(line, bino)
            predicts.append(temp_pred)
        return np.array(predicts)

    @property
    def gbdtmodel(self):
        return self.gdbt_modelparamter


if __name__ == "__main__":
    from sklearn.datasets import load_iris

    data = load_iris()['data']
    label = load_iris()['target']
    data = data[label != 1]
    label = label[label != 1]
    label = label - 1
    label = label[:, np.newaxis]

    my = XgboostTree().fit(data, label)
    pre = my.gbdt_predict(data, bino=True)
    print(pre)

    from sklearn.metrics import recall_score, confusion_matrix
    print(confusion_matrix(label.flatten(), pre))
    print(recall_score(label, pre))

