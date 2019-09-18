

class PrintBigdata:
    def __init__(self):
        pass

    def print_data_line(self, line):
        flag = 1
        lens = len(line)
        temp_index = 0
        for index in range(lens):
            if line[index] != 0 and flag == 1:
                flag = 0
                temp_index = index
                break
        if flag == 0:
            new_line = ''.join([str(i) for i in line[temp_index:]])
            print(new_line)

    def fit(self, n):
        if n < 1:
            return
        # 注意这种方法生成一个序列。
        data = [0 for _ in range(n)]
        # data = np.repeat(0, n)
        for i in range(10):
            data[0] = i
            self.print_bigdata(data, n, index=0)

    def print_bigdata(self, data, lens, index):
        if index == lens-1:
            self.print_data_line(data)
            return
        for i in range(10):
            data[index + 1] = i
            self.print_bigdata(data, lens, index=index+1)


class PrintRever(PrintBigdata):
    def __init__(self, lists=None):
        super(PrintRever).__init__()
        if lists is None:
            self.lists = range(9, -1, -1)
        else:
            lens = len(lists)
            for i in range(10):
                if i == lists[i] or i == lists[lens-i-1]:
                    self.lists = lists
                else:
                    raise ValueError

    def fit(self, n):
        if n < 1:
            return
        data = [0 for _ in range(n)]
        for i in self.lists:
            data[0] = i
            self.print_bigdata(data, n, index=0)

    def print_bigdata(self, data, lens, index):
        if index == lens-1:
            self.print_data_line(data)
            return
        for i in self.lists:
            data[index+1] = i
            self.print_bigdata(data, lens, index=index+1)


if __name__ == "__main__":
    #my = PrintBigdata()
    my = PrintRever(lists=[i for i in range(9, -1, -1)])
    my.fit(3)

