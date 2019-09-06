import numpy as np


class MyRun:
    def __init__(self, rows, cols, target=20):
        self.maxrow = rows
        self.maxcol = cols
        self.label = np.zeros(rows * cols)
        self.target = target
        self.data_list = []

    def cal_value(self, data, mode=10):
        sum = data // mode + data % mode
        return sum

    def judge(self, row, col):
        if row < self.maxrow and col < self.maxcol and col >=0 and row >= 0 \
            and self.label[row * self.maxrow + col] == 0 \
            and (self.cal_value(col) + self.cal_value(row) <= self.target):
            self.label[row * self.maxrow + col] = 1
            self.data_list.append([row, col])
            return 1
        else:
            return 0

    def cal(self, row=0, col=0):
        count = 0
        if self.judge(row, col) == 1:
            count = 1 + self.cal(row - 1, col) + self.cal(row, col - 1) + \
                        self.cal(row + 1, col) + self.cal(row, col + 1)
        return count


if __name__ == "__main__":
    my = MyRun(10, 10, target=5)
    result = my.cal(0, 0)
    print(result)
    print(my.data_list)
