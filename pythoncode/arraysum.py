

class ArrayMaxSum:
    def __init__(self):
        pass

    def cal(self, data):
        lens = len(data)
        if lens < 0:
            return 'wrong'
        # 这里最好是初始化 data的第一个数据。
        maxsum = data[0]
        sum = 0
        for i in range(lens):
            sum += data[i]
            if sum > maxsum:
                maxsum = sum
            if sum < 0:
                sum = 0
        return maxsum


if __name__ == "__main__":
    data = [1, -2, 3, 10, -4, 7, 2, -5]
    # data = [1, 2, 3, 4, 5, 6]
    # data = [-5, -2, -1, 1, 4, -5]
    my = ArrayMaxSum()
    result = my.cal(data)
    print(result)
