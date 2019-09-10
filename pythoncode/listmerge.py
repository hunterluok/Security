

class ListMerge:
    def __init__(self):
        pass

    def merge(self, data1, data2):
        i = 0
        j = 0
        len_d2 = len(data2)
        lens = len(data1)
        while i < lens and j < len_d2 and data1[i] <= data2[j]:
            index = i
            # print("index is {}".format(index))
            while index < lens and data[index] <= data2[j]:
                index += 1
            data1.insert(index, data2[j])
            lens = len(data1)
            i = index
            j += 1
        return data1


class ListMergeTwo:
    def __init__(self):
        pass

    def get_merge(self, d1, d2):
        if d1[0] > d2[0]:
            return self.merge(d2, d1, start=0, end=0)
        else:
            return self.merge(d1, d2, start=0, end=0)

    def merge(self, d1, d2, start=0, end=0):
        len1 = len(d1)
        len2 = len(d2)
        if start >= len1 or end >= len2:
            return d1

        index = start
        while index < len1 and d1[index] <= d2[end]:
            index += 1
        d1.insert(index, d2[end])
        print("end is {}".format(end))
        print("index is {}".format(index))
        self.merge(d1, d2, start=index, end=end+1)
        return d1


if __name__ == "__main__":
    #my = ListMerge()
    #data = [1, 3, 5, 7]
    #data2 = [2, 3, 4, 4, 8, 9, 10, 11]
    #print(my.merge(data, data2))

    my = ListMergeTwo()
    data = [1, 3, 5, 7]
    data2 = [2, 3, 4, 4, 8, 9, 22, 31]
    print(my.get_merge(data, data2))


