
import numpy as np

a = -np.inf
b = 0


class InversePair:
    def __init__(self):
        pass

    def get_pair(self, data):
        new = data[:]
        ends = len(data) - 1
        start = 0
        count = self.get_count(data, new, start, ends)
        print("data is {}".format(data))
        print("new is {}".format(new))
        return count

    def get_count(self, data, new, start, ends):
        if start == ends:
            new[start] = data[start]
            return 0

        length = (ends - start) // 2
        left = self.get_count(new, data, start, start+length)
        right = self.get_count(new, data, start+length+1, ends)

        count = 0
        left_index = start + length
        right_index = ends
        new_index = ends

        while left_index >= start and right_index >= start + length + 1:
            if data[left_index] > data[right_index]:
                new[new_index] = data[left_index]
                # count += right_index - start - length  统计逆序对。

                # 统计翻转对
                temp_index = right_index
                while temp_index >= start + length + 1:
                    if data[left_index] > 2 * data[temp_index]:
                        count += 1
                        print("ANOTH {}--{}".format(data[left_index], data[temp_index]))
                    temp_index -= 1

                # 统计 逆序对的 最大差值。
                p = right_index
                while start + length + 1 <= p <= right_index:
                    global a
                    diff = data[left_index] - data[p]
                    if diff > a:
                        a = diff
                    global b
                    b += 1
                    print(("--", data[left_index], data[p]), (b, "---b"))
                    p -= 1

                left_index -= 1
                new_index -= 1
            else:
                new[new_index] = data[right_index]
                new_index -= 1
                right_index -= 1

        while left_index >= start:
            new[new_index] = data[left_index]
            left_index -= 1
            new_index -= 1
        while right_index >= start + length + 1:
            new[new_index] = data[right_index]
            new_index -= 1
            right_index -= 1
        return left + right + count

    @staticmethod
    def test(data, target):
        model = InversePair()
        result = model.get_pair(data)
        if result == target:
            print("passed")
            return
        else:
            print(result)
            print("not passed")


if __name__ == "__main__":
    #data = [7, 5, 6, 4]
    data = [6, 5, 4, 3, 2, 1]
    #data = [1, 2, 3, 4, 7, 6, 5]
    my = InversePair()
    print(my.get_pair(data))
    print(data)
    print("a is {}".format(a))