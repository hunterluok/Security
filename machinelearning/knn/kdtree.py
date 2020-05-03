import numpy as np
from heapq import nsmallest


class KdNode:
    def __init__(self, data=None, value=None, feature=None, father=None, left=None, right=None):
        self.data = data
        self.value = value
        self.feature = feature
        self.father = father
        self.left = left
        self.right = right


class KdTree:
    def __init__(self):
        pass

    def split_data(self, data, feature, value):
        left = data[data[:, feature] < value]
        right = data[data[:, feature] > value]
        mid = data[data[:, feature] == value]
        return left, right, mid

    def get_feature(self, deepth, k):
        # 这里注意  feature = deepth % k + 1
        feature = deepth % k
        return feature

    def get_median(self, arraydata):
        arraydata = sorted(arraydata)
        index = int(len(arraydata) / 2)
        median = arraydata[index]
        return median

    def build_tree(self, datas, deepth=0):
        root = KdNode()
        if len(datas) == 1:
            root.data = datas
            return root

        m, n = datas.shape
        feature = self.get_feature(deepth, n)
        median = self.get_median(datas[:, feature])
        left_data, right_data, mid_data = self.split_data(datas, feature, median)

        # 节点的数据集
        root.data = mid_data
        # 切分采用的特征
        root.feature = feature
        # 切分时用的值
        root.value = median

        if len(left_data) > 0:
            root.left = self.build_tree(left_data, deepth=deepth + 1)
            root.left.father = root
        if len(right_data) > 0:
            root.right = self.build_tree(right_data, deepth=deepth + 1)
            root.right.father = root
        return root

    @classmethod
    def print_tree(cls, tree):
        if tree.data is not None:
            print(tree.data)
            print("*" * 10)
        if tree.left is not None:
            cls.print_tree(tree.left)
        if tree.right is not None:
            cls.print_tree(tree.right)


class FindK:
    def __init__(self, k=2):
        self.dist = [np.inf] * k
        self.k = k
        # self.kn = nsmallest(2, self.dist)
        self.best_node = None

    def find(self, target, tree):
        # 找到最近的节点
        trees = tree
        while trees.feature is not None:
            feature = trees.feature
            value = trees.value
            tar_val = target[:, feature]
            if tar_val < value:
                trees = trees.left
            elif tar_val > value:
                trees = trees.right
            else:
                return trees
        return trees

    def get_dist(self, data_node, target):
        da = data_node.data
        dist = np.sum(np.power(da[0] - target.flatten(), 2))
        return np.sqrt(dist)

    def find_min(self, trees, target):
        if trees.left or trees.right:
            feature = trees.feature
            value = trees.value
            if target[:, feature] < value and trees.left:
                self.find_min(trees.left, target)
            elif trees.right:
                self.find_min(trees.right, target)

        temp_dist = self.get_dist(trees, target)
        # if self.dist is None or temp_dist < self.dist:
        if self.dist is None or temp_dist < max(self.dist):
            # self.dist = temp_dist
            self.dist.append(temp_dist)
            self.dist = nsmallest(self.k, self.dist)
            self.best_node = trees

        if trees.feature is not None:
            feature = trees.feature
            value = trees.value
            # if abs(target[:, feature] - trees.data[:, feature]) < self.dist:
            if abs(target[:, feature] - trees.data[:, feature]) < np.max(self.dist):
                if trees.left and target[:, feature] >= value:
                    self.find_min(trees.left, target)
                elif trees.right and target[:, feature] < value:
                    self.find_min(trees.right, target)


if __name__ == "__main__":
    my = KdTree()

    data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2], [0, 1]])
    root = my.build_tree(data)
    my.print_tree(root)

    myf = FindK(k=1)
    target = np.array([[4, 5]])
    myf.find_min(root, target)
    d = myf.best_node

