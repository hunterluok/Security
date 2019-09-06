import numpy as np


class FindMax:
    def __init__(self):
        self.lens_list = None

    def fit(self, data):
        if data <= 1 or not isinstance(data, int):
            return "wrong"
        if data == 2:
            return 1
        if data == 3:
            return 2
        if data > 3:
            self.lens_list = np.zeros(data + 1)
            return self.fit_anther(data)

    def fit_anther(self, data):
        self.lens_list[1] = 1
        self.lens_list[2] = 2
        self.lens_list[3] = 3
        for lens in np.arange(4, data+1):
            maxs = 0
            min_len = int(lens / 2)
            # print("min_len is {}".format(min_len))
            for sub_len in np.arange(1, min_len+1):
                # print("sub_len is {}".format(sub_len))
                prod_value = self.lens_list[sub_len] * self.lens_list[lens - sub_len]
                if prod_value > maxs:
                    maxs = prod_value
            self.lens_list[lens] = maxs
        return max(self.lens_list)

    @staticmethod
    def test(func, data, target):
        result = func(data)
        print("algo result is {}".format(result))
        if result == target:
            print("passed")
        else:
            print("not passed")


if __name__ == "__main__":
    myfindmax = FindMax()
    myfindmax.test(func=myfindmax.fit, data=9, target=27)
    # print(np.power(3, 5) * 4)
    # print(np.zeros(10))

