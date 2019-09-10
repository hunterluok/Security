

class MyQueue:
    def __init__(self):
        pass

    def find(self, data, k=3):
        lens = len(data)
        if lens < k:
            return "false"

        # 存储滑动窗口的 一些列值
        max_list = []
        max_index = None
        #  存储可能的最大值
        max_value_list = []
        max_index = 0
        max_value = 0

        for i in range(lens):
            if i == 0:
                max_list.append(data[i])
                max_value_list.append(data[i])
                max_index = 0
                max_value = data[i]
            if i < 3:
                if data[i] < max_value:
                    if len(max_value_list) == 1:
                        max_value_list.append(data[i])
                    else:
                        while len(max_value_list) != 0:
                            if data[i] > max_value_list[-1]:
                                max_value_list.pop()
                        max_value_list.append(data[i])



                elif

        return max_list


if __name__ == "__main__":
    my = MyQueue()
    data = [6, 5, 4, 2, 6, 2, 5, 1]
    result = my.find(data, 3)
    print(result)

