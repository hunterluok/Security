


class myrun:
    def __init__(self, rows, cols):
        self.maxrow = rows
        self.maxcol = cols

    def cal_vale(self, data, mode=10):
        sum = data // mode + data % mode
        return sum

    def cal(self):
        pass


if __name__ == "__main__":
    print(22 % 10)
    print(22 // 10)