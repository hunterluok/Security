


class SumS:
    def __init__(self):
        pass

    def find_notsort(self, data, target):
        """
        不进行2次遍历，利用字典存储数据及其下表，利用 字典的查找实现。 适用于非排序的数据
        :param data:
        :param target:
        :return:
        """
        lens = len(data)
        if lens < 2:
            return "wrong"
        dicts = {ele: i for(ele, i) in zip(data, range(lens+1))}
        for key in dicts.keys():
            tar_ele = target - key
            if tar_ele in dicts.keys():
                print("idx is {}, idx2 is {}".format(dicts[key], dicts[tar_ele]))
                return key, tar_ele
        return None


    def find(self, data, target):
        """
        适用于排序数据
        :param data:
        :param target:
        :return:
        """
        lens = len(data)
        if lens < 2:
            return None
        # 注意这里的排序方法，否者会出现问题
        data = sorted(data)
        temp_lens = int(lens / 2)
        i = 0
        ends = lens-1
        while i < temp_lens and ends >= temp_lens:
            print("{}-{}".format(i, ends))
            if data[i] + data[ends] == target:
                return data[i], data[ends]
            elif data[i] + data[ends] < target:
                i += 1
            else:
                ends -= 1
        return None


if __name__ == "__main__":
    my = SumS()
    data = [3, 2, 4, 9, 10, 5]
    target = 13
    print(my.find_notsort(data, target))