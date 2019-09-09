

import numpy as np


class JiOuShu:
    def __init__(self):
        pass

    def findcount(self, data, flag=0):
        count = 0
        for ele in data:
            if ele % 2 == flag:
                count += 1
        return count

    def rank_f(self, data):
        lens = len(data)
        counts = self.findcount(data)
        new_list = np.repeat(0, lens)
        ou_idex = 0
        j_idex = counts
        for ele in data:
            if ele % 2 == 0:
                new_list[ou_idex] = ele
                ou_idex += 1
            else:
                new_list[j_idex] = ele
                j_idex += 1
        return new_list

    def rank(self, data):
        lens = len(data)
        counts = self.findcount(data)
        idex = 0
        max_idex = counts
        while idex < counts and max_idex < lens:
            if data[idex] % 2 != 0 and data[max_idex] % 2 == 0:
                data[idex], data[max_idex] = data[max_idex], data[idex]
            elif data[idex] % 2 != 0 and data[max_idex] % 2 != 0:
                max_idex += 1
            elif data[idex] % 2 == 0 and data[max_idex] % 2 == 0:
                idex += 1
            else:
                idex += 1
                max_idex += 1
        return data

    def rank_another(self, data):
        """
        不考虑 数字的相对顺序
        :param data:
        :return:
        """
        lens = len(data)
        # mid_lens = int(lens / 2)
        idex = 0
        max_idex = lens - 1
        while idex < max_idex:
            if data[idex] % 2 != 0 and data[max_idex] % 2 == 0:
                data[idex], data[max_idex] = data[max_idex], data[idex]
            elif data[idex] % 2 != 0 and data[max_idex] % 2 != 0:
                max_idex -= 1
            elif data[idex] % 2 == 0 and data[max_idex] % 2 == 0:
                idex += 1
            else:
                idex += 1
                max_idex -= 1
        return data


if __name__ == "__main__":
    my = JiOuShu()
    data = [2, 1, 3, 4, 5, 7, 8, 9]
    # print(my.rank_another(data))
    print(my.rank(data))
    # print(my.rank_f(data))

