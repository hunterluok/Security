
from test.treeRegression import CartreeRegression

import numpy as np


class GbdtTree(CartreeRegression):
    def __init__(self, n_trees=10, max_depth=10, ifmaxbins=False):
        super(GbdtTree, self).__init__()
        self.n_trees = n_trees
        self.ifmaxbins = ifmaxbins
        self.max_depth = max_depth

    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def __predict_line(self, model, line):
        if model.label_class is not None:
            return model.label_class, model
        split_feature = model.feature
        split_value = model.value
        if line[split_feature] > split_value:
            return self.__predict_line(model.right_tree, line)
        else:
            return self.__predict_line(model.left_tree, line)

    def __get_gama(self, data, mytree):
        last = {}
        for index, line in enumerate(data):
            x, y = line[:-1], line[-1]
            temp_label, temp_node = self.__predict_line(mytree, x)
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
        f0 = 0.5 * np.log((1 + np.mean(target))/(1 - np.mean(target)))
        fx = np.repeat(f0, m).reshape((m, 1))

        pred_dict = {}
        pred_dict.setdefault("init_fx", f0)

        for i in range(self.n_trees):
            dety = 2 * target / (1 + np.exp(2 * np.multiply(target, fx)))
            newdata = np.concatenate([data, dety.reshape(m, 1)], axis=1)
            mymodel = CartreeRegression(min_leafs=3, ifmaxbins=self.ifmaxbins, max_depth=self.max_depth)
            mytree = mymodel.createTree(newdata)
            print("carttree deep is {}".format(mymodel.get_deep(mytree)))

            gama_list, node_gama = self.__get_gama(newdata, mytree)
            fx = fx + gama_list[:, 1:2]
            #存储模型的参数
            pred_dict.setdefault("tree", []).append(mytree)
            pred_dict.setdefault("local_gama", []).append(node_gama)
        self.gdbt_modelparamter = pred_dict
        return self

    def gbdt_predict_line(self, line):
        init_f0 = self.gdbt_modelparamter['init_fx']
        tree_list = self.gdbt_modelparamter['tree']
        local_gama_list = self.gdbt_modelparamter['local_gama']

        for tree, local_gama in zip(tree_list, local_gama_list):
            temp_pred, node = self.__predict_line(tree, line)
            gama = local_gama[node]
            init_f0 += gama
        last_pred = 1 if self.__sigmoid(init_f0) > 0.5 else -1
        return last_pred

    def gbdt_predict(self, data):
        predicts = []
        for line in data:
            temp_pred = self.gbdt_predict_line(line)
            predicts.append(temp_pred)
        return np.array(predicts)

    @property
    def gbdtmodel(self):
        return self.gdbt_modelparamter

