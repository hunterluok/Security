

class FirstAppear:
    def __init__(self):
        pass

    def cal(self, data):
        lens = len(data)
        if lens < 1:
            return "No"
        dicts = {}
        for ele in data:
            dicts.setdefault(ele, 0)
            dicts[ele] += 1
        for key in dicts.keys():
            if dicts[key] == 1:
                return key
        return "NO"

    @staticmethod
    def test(func, data, target):
        result = func(data)
        print("result is {}".format(result))
        if result == target:
            print("passed")
        else:
            print("no passed")


class FirshAppearTwo(FirstAppear):
    def __init__(self):
        super(FirstAppear, self).__init__()
        pass

    def cal(self, data):
        pass


if __name__ == "__main__":
    my = FirstAppear()
    data = ['a', 'a', 'a', 'c', 'a']
    # target = 'b'
    target = 'c'
    # print(my.cal(data))
    my.test(my.cal, data, target)