

class MyQueue:
    def __init__(self):
        pass

    def find(self, data, k=3):
        lens = len(data)
        if lens < k:
            return "false"

        max_list = []
        temp_data = data[:k]
        maxs = max(temp_data)
        max_list.append(maxs)
        for i in range(k, lens):
            if data[i] > maxs:
                max_list.append(data[i])
                maxs = data[i]
            else:
                max_list.append(maxs)
        return max_list


if __name__ == "__main__":
    my = MyQueue()
    data = [2, 3, 4, 2, 6, 2, 5, 1]
    result = my.find(data, 3)
    print(result)

