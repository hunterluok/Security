

class CharExchange:
    def __init__(self):
        pass

    def get(self, data):
        lens = len(data)
        first = [data[0]]
        second = data[1:]
        self.another(first, second)
        for i in range(1, lens):
            data[0], data[i] = data[i], data[0]
            self.another([data[0]], data[1:])

    def another(self, first, second):
        print(first + second)
        print(first + self.fit(second))
        # print(first.append(second))
        # print(first.append(self.fit(second)))

    def fit(self, data):
        if len(data)== 2:
            data[0], data[1] = data[1], data[0]


class AllRank(CharExchange):
    def __init__(self):
        super(AllRank, self).__init__()
        pass

    def rank(self, data):
        lists = data
        if len(data) == 3:
            first = [data[0]]
            second = self.fit(data[1:])
            temp = first + second
            lists.append(temp)
        return lists


if __name__ == "__main__":
    my = CharExchange()
    data = ['a', 'b', 'c']#, 'd']
    my.get(data)

