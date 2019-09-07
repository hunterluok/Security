

class FindMinK:
    def __init__(self):
        pass

    def find(self, data, k):
        lens = len(data)
        # if k < 1:
        #     return "wrong"
        if lens < k or k < 1:
            return []
        last_list = data[:k]
        for i in range(k, lens):
            temp_data = data[i]
            maxs = max(last_list)
            if temp_data < maxs:
                last_list.remove(maxs)
                last_list.append(temp_data)
        last_list = sorted(last_list)
        return last_list


if __name__ == "__main__":
    my = FindMinK()
    data = [4, 5, 1, 6, 2, 7, 3, 8]
    result = my.find(data, 4)
    print(result)
