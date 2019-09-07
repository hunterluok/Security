

class Stack:
    def __init__(self):
        pass

    def get_max(self, data):
        lens = len(data)
        if lens < 1:
            return "wrong"

        min = data[0]
        max_reven = 0
        max = 0
        for i in range(lens):
            temp = data[i]
            temp_value = temp - min
            if temp_value > max_reven:
                max_reven = temp_value
                max = temp
            else:
                min = temp
        print("max is {}, min is {}, max_value is {}".format(max, min, max_reven))
        return max_reven

    @staticmethod
    def test(func, data, target):
        result = func(data)
        print("result is {}".format(result))
        if result == target:
            print("passed")
        else:
            print("not passed")


if __name__ == "__main__":
    my = Stack()
    # data = [5, 4, 3, 7, 9]
    # data = []
    # data = [1, 2, 3, 5, 6]
    data = [6, 5, 4, 3, 2, 1]
    data = [3, 2]
    data = [2, 3]
    #print(my.get_max(data))
    my.test(my.get_max, data, 6)

