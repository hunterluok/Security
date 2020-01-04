
import numpy as np

from test.trees.treeRegression import CartreeRegression


class GbdtTree:
    """
    解决 二分类问题。
    """
    def __init__(self, n_trees=100, max_depth=10, ifmaxbins=False):
        self.n_trees = n_trees
        self.ifmaxbins = ifmaxbins
        self.max_depth = max_depth

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

    def __get_gama(self, data, mytree, target=None):
        last = {}
        for index, line in enumerate(data):
            x, y = line[:-1], line[-1]
            temp_label, temp_node = self.predict_line(mytree, x)
            last.setdefault(temp_node, {})
            last[temp_node].setdefault("index", []).append(index)
            last[temp_node].setdefault("fz", 0)
            last[temp_node]['fz'] += y
            last[temp_node].setdefault("fm", 0)
            last[temp_node]['fm'] += np.abs(y) * (2 - np.abs(y))
        # 每个样本 对应的 gama值，每个node 下的样本的gama值一样， 用于train, ml=>gama_list
        ml = {}
        # 每个node 的gama值，用于预测时
        new_last = {}
        for key, value in last.items():
            index_list = value['index']
            gama = value['fz'] / value['fm']
            new_last.setdefault(key, gama)
            for idx in index_list:
                ml.setdefault(idx, gama)
        gama_list = np.array([[int(i[0]), i[1]] for i in sorted(ml.items(), key=lambda row: row[0])])
        return gama_list, new_last

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
            newdata = np.concatenate([data, dety.reshape(m, 1)], axis=1)
            mymodel = CartreeRegression(min_leafs=3, max_depth=self.max_depth)
            mytree = mymodel.createTree(newdata)
            # print("carttree deep is {}".format(mymodel.get_deep(mytree)))
            gama_list, node_gama = self.__get_gama(newdata, mytree)
            fx = fx + gama_list[:, 1:2]
            #存储模型的参数
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
            last_pred = 1 if self.__sigmoid(init_f0) > self.__sigmoid(-init_f0) else -1
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


class LgbTreeLda(GbdtTree):
    def __init__(self,
                 min_leafs=4,
                 max_depth=20):
        super().__init__()
        self.min_leafs = min_leafs
        self.max_depth = max_depth

    # 这个地方有点问题， 应该在训练模型的时候 记录叶子节点的 标号等。
    def __get_gama(self, data, mytree, target=None):
        last = {}
        for index, line in enumerate(data):
            x, y = line[:-1], line[-1]
            temp_label, temp_node = self.predict_line(mytree, x)
            last.setdefault(temp_node, {})
            last[temp_node].setdefault("index", []).append(index)
            # 此处用来求 各个节点的  gama值
            last[temp_node].setdefault("fz", []).append(target[index])

        # 每个样本 对应的 gama值，每个node 下的样本的gama值一样， 用于train, ml=>gama_list
        ml = {}
        # 每个node 的gama值，用于预测时
        new_last = {}
        for key, value in last.items():
            index_list = value['index']
            gama = np.median(value['fz'])
            new_last.setdefault(key, gama)
            for idx in index_list:
                ml.setdefault(idx, gama)
        gama_list = np.array([[int(i[0]), i[1]] for i in sorted(ml.items(), key=lambda row: row[0])])
        return gama_list, new_last

    def fit(self, data, target):
        m, n = data.shape

        if len(target.shape) != 2:
            target = target.reshape(m, 1)

        # 初始化某些值
        # f0 = 0.5 * np.log((1 + np.mean(target))/(1 - np.mean(target)))
        f0 = np.median(target)
        fx = np.repeat(f0, m).reshape((m, 1))

        pred_dict = {}
        pred_dict.setdefault("init_fx", f0)

        for i in range(self.n_trees):
            # dety = 2 * target / (1 + np.exp(2 * np.multiply(target, fx)))
            dety = np.sign(target - fx)

            newdata = np.concatenate([data, dety.reshape(m, 1)], axis=1)
            mymodel = CartreeRegression(min_leafs=self.min_leafs, max_depth=self.max_depth)
            mytree = mymodel.createTree(newdata)
            print("carttree deep is {}".format(mymodel.get_deep(mytree)))

            gama_list, node_gama = self.__get_gama(newdata, mytree, target-fx)
            fx = fx + gama_list[:, 1:2]

            #存储模型的参数
            pred_dict.setdefault("tree", []).append(mytree)
            pred_dict.setdefault("local_gama", []).append(node_gama)
        self.gdbt_modelparamter = pred_dict
        return self


if __name__ == "__main__":
    from sklearn.datasets import load_iris
    data = load_iris()['data']
    label = load_iris()['target']

    data = data[label != 1]
    label = label[label != 1]

    label = label - 1
    label = label[:, np.newaxis]

    my = GbdtTree().fit(data, label)
    pre = my.gbdt_predict(data, bino=True)
    print(pre)

    from sklearn.metrics import recall_score, confusion_matrix
    print(confusion_matrix(label.flatten(), pre))
    print(recall_score(label, pre))
