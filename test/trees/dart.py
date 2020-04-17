
import numpy as np
import random

from test.trees.treeRegression import Tree, treeNode
from test.trees.xgboost import TreeBase


class XgboostTree:
    """
    解决 二分类问题。
    """
    def __init__(self,
                 n_trees=100,
                 max_depth=10,
                 verbose=False,
                 dropout=0.9):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.verbose = verbose
        self.lmds = 0.4
        self.gama = 0.5
        self.dropout = dropout

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

        mt = {}
        mt.setdefault(0, fx)

        for ntree in range(1, self.n_trees + 1):

            # drop 获取
            lens = len(mt)
            sub_len = int(self.dropout * lens)
            if sub_len < 1:
                index = [np.random.randint(0, lens)]
            else:
                index_list = np.arange(lens)
                random.shuffle(index_list)
                index = index_list[:sub_len]

            nfx = np.sum([mt[i] for i in index])

            dety = 2 * target / (1 + np.exp(2 * np.multiply(target, nfx)))
            # 损失函数的 二阶倒数
            h = np.multiply(-2 * target / (1 + np.exp(-2 * np.multiply(target, fx))), dety)

            label = np.concatenate([dety, h], axis=1)
            mymodel = TreeBase(min_leafs=3, max_depth=self.max_depth)
            mytree = mymodel.createTree(data, label)

            # print("carttree deep is {}".format(mymodel.get_deep(mytree)))
            gama_list, node_gama, loss = self.__get_gama(data, mytree, target=label)
            if self.verbose:
                print("loss at {} is {}".format(ntree, loss))

            target = gama_list[:, 1:2]
            # mt.setdefault(ntree, target * 1 / (len(index) + 1))

            # 规范化。
            factor = len(index) / (len(index) + 1)
            mt = {k: (v / factor) for k, v in mt.items()}
            mt.setdefault(ntree, target * 1 / (len(index) + 1))

            # 存储模型的参数
            pred_dict.setdefault("tree", []).append(mytree)
            pred_dict.setdefault("local_gama", []).append(node_gama)
        self.gdbt_modelparamter = pred_dict
        print(mt)
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

