

from multiprocessing import Queue, Process
import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
import time
import random


class mytree:
    def __init__(self, feature=-1, value=None, left_tree=None, right_tree=None, label_class=None):
        self.feature = feature
        self.value = value
        self.left_tree = left_tree
        self.right_tree = right_tree
        self.label_class = label_class

    @staticmethod
    def __name__():
        """
        type(mytreemodel).__name__ == "treenode"
        :return: treeode, 可能有用，也可能没有用处，暂时放着，有空研究
        """
        return "treenode"


class mycarttree:
    def __init__(self, min_leafs):
        self.min_leafs = min_leafs

    def calculate_gini(self, label):
        temp_dicts = {}
        for temp_label in label:
            temp_label = temp_label[0]
            temp_dicts.setdefault(temp_label, 0)
            temp_dicts[temp_label] += 1

        temp_count = np.array([i for i in temp_dicts.values()])
        sum_values = np.sum(temp_count)
        gini_value = 1 - np.sum(np.power(temp_count / sum_values, 2))
        return gini_value

    def split_data(self, data, feature, value, label):
        if not label.shape:
            raise TypeError("label muste be two dim")
        condition_left = data[:, feature] <= value
        condition_right = data[:, feature] > value

        left_data = data[condition_left]
        right_data = data[condition_right]
        left_label = label[condition_left]
        right_label = label[condition_right]
        return left_data, left_label, right_data, right_label

    def find_best_split(self, data, label):
        """
        只需要 寻找到切分点，不需要切分数据，否则太麻烦
        :param data:
        :param label:
        :return:
        """
        m, n = data.shape
        best_feature = None
        best_feature_value = None
        best_left_data = None
        best_right_data = None
        best_left_label = None
        best_right_label = None

        max_ginigain = 0
        init_gini = self.calculate_gini(label)

        for feature_index in range(n):
            feature_values = set(data[:, feature_index])
            for feature_value in feature_values:
                left_data, left_label, right_data, right_label = self.split_data(data, feature_index, feature_value, label)
                split_gini = (left_label.shape[0] / m) * self.calculate_gini(left_label) + (right_label.shape[
                                                                       0] / m) * self.calculate_gini(right_label)

                temp_ginigain = init_gini - split_gini
                if temp_ginigain > max_ginigain:
                # 在这里使用 叶子数量作为 是否跟新不太合适。
                # and len(left_data) >= self.min_leafs and len(right_data) >= self.min_leafs:
                    max_ginigain = temp_ginigain
                    best_feature = feature_index
                    best_feature_value = feature_value
                    best_left_data = left_data
                    best_right_data = right_data
                    best_left_label = left_label
                    best_right_label = right_label
        return best_feature, best_feature_value, best_left_data, best_right_data, best_left_label, best_right_label

    def get_result(self, label):
        return Counter([i[0] for i in label]).most_common()[0][0]

    def fit(self, data, label):
        another_node = mytree()
        if len(np.unique(label)) == 1 or data.shape[0] < self.min_leafs:
            another_node.label_class = self.get_result(label)
            return another_node

        best_feature, best_feature_value, best_left_data, best_right_data, best_left_label, best_right_label = self.find_best_split(
            data, label)

        if best_feature is None:
            another_node.label_class = self.get_result(label)
            return another_node

        right = self.fit(best_right_data, best_right_label)
        left = self.fit(best_left_data, best_left_label)
        another_node.feature = best_feature
        another_node.value = best_feature_value
        another_node.left_tree = left
        another_node.right_tree = right
        return another_node

    # @staticmethod
    @classmethod
    def predict_line(cls, model, line, high=0):
        if model.label_class is not None:
            return model.label_class
        split_feature = model.feature
        split_value = model.value

        temp_value = line[split_feature]
        if temp_value <= split_value:
            # 这里需要注意的是 与上面划分保持一致就好了。
            return cls.predict_line(model.left_tree, line, high=high + 1)
        else:
            return cls.predict_line(model.right_tree, line, high=high + 1)

    @classmethod
    def predict(cls, model, data):
        myre = []
        for line in data:
            te = cls.predict_line(model, line)
            myre.append(te)
        myre = np.array(myre).reshape(len(data), 1)
        return myre

    @classmethod
    def print_leafs(cls, model):
        """
        :param model:
        :return: 树的 叶子节点
        """
        if model.label_class is not None:
            print("leaf is {} ".format(model.label_class))
        if model.left_tree is not None:
            cls.print_leafs(model.left_tree)
        if model.right_tree is not None:
            cls.print_leafs(model.right_tree)

    @classmethod
    def get_treedeep(cls, model):
        max_dep = 0
        if model.left_tree is not None:
            temp_dep = 1 + cls.get_treedeep(model.left_tree)
            if temp_dep > max_dep:
                max_dep = temp_dep
        if model.right_tree is not None:
            temp_dep = 1 + cls.get_treedeep(model.right_tree)
            if temp_dep > max_dep:
                max_dep = temp_dep
        return max_dep


def single_model(data, label, ratio=0.9):
    """
    对数据进行划分
    :param data:
    :param label:
    :param ratio:
    :return:
    """
    m, n = data.shape
    index = np.arange(m)
    random.shuffle(index)
    #index = np.random.permutation(np.arange(m))
    # feature_index = np.random.permutation(np.arange(n))
    nums = index[:int(ratio * m)]
    n_data = data[nums]
    n_label = label[nums]
    return n_data, n_label


def myjob(q, q_acc, r, data, mylabel):
    # r = np.random.uniform(0.8, 1)
    # 这种搞随机数是不可行的，
    my_data, my_label = single_model(data, mylabel, ratio=r)
    mymodel = mycarttree(2)
    result = mymodel.fit(my_data, my_label)

    m, _ = data.shape
    preds = mymodel.predict(result, data)
    acc = np.round(np.sum(preds == mylabel) / m, 4)
    print("this model's acc is {}".format(acc))
    q.put(preds)
    q_acc.put(acc)


def get_label(nps_data):
    last_label = []
    for line in nps_data:
        temp_label = Counter(line).most_common()[0][0]
        last_label.append([temp_label])
    return np.array(last_label)


if __name__ == "__main__":
    # data = load_iris()['data']
    # mylabel = load_iris()['target']
    # mylabel = np.array([[i] for i in mylabel])
    # mymodel = mycarttree(2)
    # result = mymodel.fit(data, mylabel)
    # preds = mymodel.predict(result, data)
    # acc = np.round(np.sum(preds == mylabel) / 150, 4)
    # print("acc is {}".format(acc))
    # print("leafs \n")
    # mymodel.print_leafs(result)
    # print("name is {}".format(type(result.left_tree).__name__))
    # print("tree max_deep is : ", mymodel.get_treedeep(result))
    # print("ok")
    #
    #
    # start = time.time()
    # q = Queue()
    # q_acc = Queue()
    # myqueus = []
    #
    # rlist = [0.8, 0.85, 0.9, 0.95, 0.75, 0.7, 1.0]
    # len_rlist = len(rlist)
    # for i, r in zip(np.arange(len_rlist), rlist):
    #     temp_job = Process(target=myjob, args=(q, q_acc, r, data, mylabel), name="jon_{}".format(i))
    #     myqueus.append(temp_job)
    #
    # for jons in myqueus:
    #     jons.start()
    #     #jons.join()  #放在这里 类似与单进程，时间长 0.3776
    #
    # for jons in myqueus:
    #    jons.join()  # 时间是0.124
    #
    # nps = -1 * np.ones((150, 1))
    # # for myres in q.get()； 这里的是读取进程中的数据
    # for _ in range(len_rlist):
    #     nps = np.concatenate([nps, q.get()], axis=1)
    #     # nps.append(q.get())
    #
    # for _ in range(len_rlist):
    #     single_acc = q_acc.get()
    #     print("sing_acc is {}".format(single_acc))
    #
    # last_label = get_label(nps)
    # acc = np.round(np.sum(last_label == mylabel) / 150, 4)
    # print("last_label acc is {}".format(acc))
    # ends = time.time() - start
    # print("use time total {}".format(ends))

    from sklearn import datasets
    from random import shuffle
    boston = datasets.load_boston()
    X, y = shuffle(boston.data, boston.target, random_state=13)
    X = X.astype(np.float32)
    offset = int(X.shape[0] * 0.9)
    x_train, y_train = X[:offset], y[:offset]
    x_test, y_test = X[offset:], y[offset:]
