

import numpy as np


class Search:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.label = np.zeros(rows * cols)

    def find(self, data, start=0, end=0, target='abcd'):
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

    def find_another(self, data, target='abcd'):
        length = 0
        for col in range(self.rows):
            for row in range(self.rows):
                if self.fit_another(data, row, col, length, target):
                    print("find it")
                    return True
        print("not find it")
        return False

    def fit_another(self, data, start, end, length, target):
        if len(target) == length:
            return True
        has_path = False
        if start < self.rows and end < self.cols and start >= 0 and end >= 0 \
                and self.label[start * self.rows + end] == 0 \
                and target[length] == data[start][end]:
            length += 1
            self.label[start * self.rows + end] = 1

            has_path = self.fit_another(data, start, end-1, length, target) | \
                self.fit_another(data, start, end+1, length, target) | \
                self.fit_another(data, start-1, end, length, target) | \
                self.fit_another(data, start+1, end, length, target)
            if not has_path:
                length -= 1
                self.label[start * self.rows + end] = 0
        return has_path


if __name__ == "__main__":
    data = np.array([['a', 'b', 'e'], ['f', 'c', 'd'], ['g', 'x', 'h']])
    my = Search()
    result = my.find_another(data)
    print(result)

