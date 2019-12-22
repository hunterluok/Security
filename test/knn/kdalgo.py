import numpy as np

from pythoncode.node import KdNode


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


class findk:
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
        return dist


    def find_min(self, trees, data_node, target):
        min_dis = self.get_dist(data_node, target)
        if data_node.father is not None:

            father_node = data_node.father
            if father_node.left == data_node:
                if father_node.right is not None:
                    pass



if __name__ == "__main__":
    my = KdTree()

    data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])

    print(my.get_median(data[:, 1]))
    root = my.build_tree(data)
    my.print_tree(root)

    news = findk()
    result = news.find(target=np.array([[3, 7]]), tree=root)
    print("--"*10)
    print(result.data)
    print(result.father.father.data)

    print(news.get_dist(result, target=np.array([[3, 7]])))

