

class MyQueue:
    def __init__(self, k):
        self.k = k

    def find(self, data):
        lens = len(data)
        if lens < self.k:
            return "false"

        # 存储滑动窗口的 一些列值, 这些需要输出的东西
        max_list = []
        #  存储可能的最大值, 最大值在0， 其他的是可能的最大值，当长度为3时清空第一个最大值。
        max_value_list = []
        max_index_list = []

        for i in range(lens):
            if i == 0:
                max_list.append(data[i])
                max_value_list.append(data[i])
                max_index_list.append(i)
            elif i < self.k:
                # i >= 1
                temp = data[i]
                if temp <= max_value_list[0]:
                    if len(max_value_list) == 1:
                        max_value_list.append(temp)
                        max_index_list.append(i)
                    else:
                        while len(max_value_list) != 0:
                            if temp >= max_value_list[-1]:
                                max_value_list.pop()
                                max_index_list.pop()
                            else:
                                break
                            max_value_list.append(temp)
                            max_index_list.append(i)
                else:
                    max_list = []
                    max_list.append(temp)
                    max_value_list = []
                    max_value_list.append(temp)
                    max_index_list = []
                    max_index_list.append(i)
            else:
                if data[i] < max_value_list[-1]:
                    if i - max_index_list[0] == self.k:
                        max_value_list = max_value_list[1:]
                        max_value_list.append(data[i])
                        max_index_list = max_index_list[1:]
                        max_index_list.append(i)
                        # 追加数据
                        max_list.append(max_value_list[0])
                        print("3. value list is {}, index is {}".format(max_value_list, max_index_list))
                    else:
                        max_value_list.append(data[i])
                        max_index_list.append(i)
                        # 追加数据
                        max_list.append(max_value_list[0])
                        print("2. value list is {}, index is {}".format(max_value_list, max_index_list))
                else:
                    # 这里需要注意，决定成败。这里先不需要追加数据。
                    if i - max_index_list[0] == self.k:
                        max_value_list = max_value_list[1:]
                        max_index_list = max_index_list[1:]
                    while len(max_value_list) != 0 and data[i] > max_value_list[-1]:
                            max_value_list.pop()
                            max_index_list.pop()
                    max_value_list.append(data[i])
                    max_index_list.append(i)
                    # 追加数据
                    max_list.append(max_value_list[0])
                    print("1. value list is {}, index is {}".format(max_value_list, max_index_list))
        print(max_value_list)
        return max_list


if __name__ == "__main__":
    my = MyQueue(k=3)
    data = [6, 7, 4, 6, 5, 2, 5, 1, 4, 3, 2, 11]
    result = my.find(data)
    print(result)

