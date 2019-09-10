

import numpy as np


class Search:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.label = np.zeros(rows * cols)

    def find(self, data, start=0, end=0, target='abcds'):
        """
        data = np.array([[a, b, x],[x, c, d], [x,x,x]])
        :param data:
        :return:
        """
        begs = ''
        # self.fit 这个函数一次只能调用一次，否则会出现问题的。
        temp = self.fit(data, start, end)
        if temp != 'x':
            begs = temp + self.find(data, start - 1, end, target) + \
                   self.find(data, start + 1, end, target) + \
                   self.find(data, start, end - 1, target) + \
                   self.find(data, start, end + 1, target)
        if begs == target:
            return "ok"
        return begs

    def fit(self, data, start, end):
        if start < self.rows and end < self.cols and start >= 0 and end >= 0 \
                and self.label[start * self.rows + end] == 0:
            temp = data[start][end]
            self.label[start * self.rows + end] = 1
            # print("temp_str is {}".format(temp))
            #if temp != 'x':
                # print("temp_str is {}".format(temp))
            return temp
        return 'x'


if __name__ == "__main__":
    data = np.array([['a', 'b', 'x'], ['x', 'c', 'd'], ['x', 'x', 'x']])
    my = Search()
    result = my.find(data)
    print(result)

