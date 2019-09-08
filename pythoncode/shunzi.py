

import numpy as np
import random


class MyShunzi:
    def __init__(self, lens=14, data=None):
        self.lens = lens
        if data is None:
            self.data = self.construct_data()
            random.shuffle(self.data)
        else:
            self.data = data

    def construct_data(self):
        a = range(0, self.lens)
        data = np.repeat(a, 4)
        return data

    def compare(self, k=5):
        if len(self.data) < k:
            return "wrong"

        temp_data = self.data[:k]
        # 先从小到大 进行排序。
        temp_data = sorted(temp_data)
        print("sored data is {}".format(temp_data))

        count_0 = 0
        count_tip = 0
        for idx in range(k):
            # 因为排序过, 所以这里的 前面的都是0。
            if temp_data[idx] == 0:
                count_0 += 1
            else:
                if idx < k-1:
                # 这里需要判断对子是不是王， 其一, 合成上面的 就需要判断 是不是为 王了
                # 这里需要判断 temp_data[idx] 不为0的情况，否者 出现其他情况
                    big = temp_data[idx + 1]
                    small = temp_data[idx]
                    if big == small:
                        print("存在对子 {}-{}".format(small, big))
                        return False
                    if big - small >= 2:
                        count_tip = big - small - 1
        if count_tip <= count_0:
            return True
        else:
            return False


if __name__ == "__main__":
    #data = [1, 0, 2, 0, 10, 2, 1, 5]
    my = MyShunzi()
    data = my.data
    print(data)
    print(my.compare(6))

