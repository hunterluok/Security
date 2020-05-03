import numpy as np

from pythoncode.node import KdNode


class BallTree:
    def __init__(self):
        pass

    def l2_norm(self, v1, v2):
        return np.sqrt(np.sum(np.power(v1 - v2, 2)))

    def get_2center(self, centor, data):
        result = np.sqrt(np.sum(np.power(centor - data, 2), axis=1))
        r_dist = np.max(result)
        r_index = list(result).index(r_dist)
        center_1 = data[r_index]
        return center_1

    def cal_r(self, centor, data):
        result = np.sqrt(np.sum(np.power(centor - data, 2), axis=1))
        r_dist = np.max(result)
        return r_dist

    def split_data(self, data):
        centor = np.mean(data, axis=0)
        center_1 = self.get_2center(centor, data)
        center_2 = self.get_2center(center_1, data)

        sub_1 = []
        sub_2 = []
        for line in data:
            dist_1 = self.l2_norm(line, center_1)
            dist_2 = self.l2_norm(line, center_2)
            if dist_1 < dist_2:
                sub_1.append(line)
            else:
                sub_2.append(line)
        return np.array(sub_1), np.array(sub_2)

    def build_tree(self, data):
        root = KdNode()
        root.value = np.mean(data, axis=0)
        root.feature = self.cal_r(np.mean(data, axis=0), data)
        if len(data) < 3:
            root.data = data
            return root
        sub_1, sub_2 = self.split_data(data)
        root.left = self.build_tree(sub_1)
        root.right = self.build_tree(sub_2)
        return root


if __name__ == "__main__":
    data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2], [0, 1]])
    mys = BallTree()
    bt = mys.build_tree(data)
    print(bt.feature)
    # bt.right.right.right.feature
    # bt.right.left.data
    # bt.right.right.left.value
    # bt.left.data
