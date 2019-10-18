
import numpy as np

from pythoncode.node import BinaryTreeNode


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
        root = BinaryTreeNode()
        if len(datas) == 1:
            root.data = datas
            return root

        m, n = datas.shape
        feature = self.get_feature(deepth, n)
        median = self.get_median(datas[:, feature])
        left_data, right_data, mid_data = self.split_data(datas, feature, median)

        root.data = mid_data
        if len(left_data) > 0:
            root.left = self.build_tree(left_data, deepth=deepth+1)
        if len(right_data) > 0:
            root.right = self.build_tree(right_data, deepth=deepth+1)
        return root

    @classmethod
    def print_tree(cls, tree):
        if tree.data is not None:
            print(tree.data)
            print("*"*10)
        if tree.left is not None:
            cls.print_tree(tree.left)
        if tree.right is not None:
            cls.print_tree(tree.right)

if __name__ == "__main__":
    my = KdTree()

    data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])

    print(my.get_median(data[:, 1]))

    root = my.build_tree(data)
    my.print_tree(root)



