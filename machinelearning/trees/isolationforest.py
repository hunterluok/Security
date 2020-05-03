

import numpy as np
import random


class TreeNode:
    def __init__(self,
                 value=None,
                 feature=None,
                 left=None,
                 right=None,
                 score=None):
        self.value = value
        self.feature = feature
        self.left = left
        self.right = right
        # 直接在节点 存储异常得分
        self.score = score


class ITree:
    def __init__(self,
                 maxbins=20,
                 minleafs=10,
                 sub_sample=0.8,
                 maxtrees=100,
                 score=True):
        self.maxbins = maxbins
        self.minleafs = minleafs
        self.sub_sample = sub_sample
        self.score = score
        self.constant = 0.5772156649

        if maxtrees < 10:
            self.maxtrees = 100
        else:
            self.maxtrees = maxtrees
        self.trees = []

    def split(self, data, val, feature):
        cond = data[:, feature] < val
        left_data = data[cond]
        right_data = data[~cond]
        return left_data, right_data

    def choose(self, data):
        m, n = data.shape
        feature = np.random.randint(0, n)
        mins, maxs = min(data[:, feature]), max(data[:, feature])
        interval = (maxs - mins) / self.maxbins
        value = np.random.randint(0, self.maxbins) * interval + mins
        return feature, value

    def build_itree(self, data, maxdeep, deep=0):
        node = TreeNode()
        if deep >= maxdeep or data.shape[0] < self.minleafs:
            # 这里的得分需要注意
            avg_deep = deep + self.get_avgdeep(data.shape[0])
            node.score = avg_deep
            return node

        feat, val = self.choose(data)
        lset, rset = self.split(data, val, feat)
        node.feature = feat
        node.value = val
        node.left = self.build_itree(lset, maxdeep, deep=deep + 1)
        node.right = self.build_itree(rset, maxdeep, deep=deep + 1)
        return node

    def get_avgdeep(self, m):
        if m < 2:
            return 1
        else:
            h = 2 * (np.log(m - 1) + self.constant) - 2 * (m - 1) / m
            return h

    def get_maxdeep(self, m):
        return np.ceil(np.log2(m))

    def fit(self, data):
        m, n = data.shape
        sub_m = []
        for i in range(self.maxtrees):
            sub_index = np.arange(m)
            random.shuffle(sub_index)
            new_m = int(self.sub_sample * m)
            sub_m.append(new_m)
            sub_index = sub_index[: new_m]
            sub_data = data[sub_index]
            max_deep = self.get_maxdeep(new_m)
            self.trees.append(self.build_itree(sub_data, max_deep, deep=0))
        self.cn = self.get_avgdeep(np.mean(m))
        return self

    def single_tree_pred(self, line, subtree):
        tree = subtree
        while tree.feature is not None:
            feat = tree.feature
            val = tree.value
            if val < line[feat]:
                tree = tree.right
            else:
                tree = tree.left
        if tree.score is not None:
            return tree.score
        else:
            raise ValueError("tree error")

    def predict_line(self, line):
        ano_score = 0
        for tree in self.trees:
            ano_score += self.single_tree_pred(line, tree)
        h = np.round(ano_score / self.maxtrees, 4)
        s = np.power(2, -1 * h / self.cn)
        if not self.score:
            if s > 0.499:
                return -1
            else:
                return 1
        return s

    def predict(self, data):
        pred = []
        for line in data:
            pred.append(self.predict_line(line))
        return pred

