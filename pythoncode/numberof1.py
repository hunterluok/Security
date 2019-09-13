

class Numberof1:
    def __init__(self, start=0):
        self.start = start

    def cal(self, n):
        count = 0
        for i in range(self.start, n+1):
            count += self.fit(i)
        return count

    def fit(self, n):
        count = 0
        while n != 0:
            if n % 10 == 1:
                count += 1
            n = n // 10
        return count


class Numof1New:
    def __init__(self):
        pass

    def cal(self, data):
        if data < 10:
            return 1
        if data < 100:
            first = data // 10 + 1
            second = 9
            third = 1
            return first + second + third
        if data < 1000:
            pass


if __name__ == "__main__":
    data = 99999
    my = Numberof1(start=0)
    result = my.cal(data)
    print(result)
    print(300 + 1000 + 9 * 280 + 9 * 19 + 9)

