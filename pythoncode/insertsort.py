

class SortAlgorithm:
    def __init__(self, data):
        self.data = data
        self.lens = len(data)

    @staticmethod
    def insert_sort(data):
        lens = len(data)
        if lens < 2:
            return data
        for i in range(1, lens):
            key = data[i]
            index = i - 1
            while index > -1 and key < data[index]:
                data[index+1] = data[index]
                index -= 1
            data[index+1] = key
        return data

    @staticmethod
    def bubble_sort(data):
        lens = len(data)
        if lens < 2:
            return data

        index = lens
        while index > 1:
            for i in range(index - 1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
            index -= 1
        return data

    def __quicksort(self, start, ends):
        # xiao -> data
        key = self.data[ends]
        i = start - 1
        for j in range(0, ends):
            if self.data[j] <= key:
                self.data[i+1], self.data[j] = self.data[j], self.data[i+1]
                i += 1
        self.data[i+1], self.data[ends] = self.data[ends], self.data[i+1]
        return i+1

    def quicksort(self, start=0, ends=5):
        # lens = len(self.data)
        #if start < ends:
        position = self.__quicksort(start, ends)
        if position - 1 > 0:
            self.quicksort(0, position - 1)
        if position + 1 < ends :
            self.quicksort(position + 1, ends)
        # self._quicksort(0, position)
        # self._quicksort(position+1, self.lens-1)

    @property
    def sort_data(self):
        return self.data


if __name__ == "__main__":
    data = [6, 2, 4, 3, 7, 1, 8, 9, 4]
    # data = [5, 4, 2, 1]

    print(SortAlgorithm.insert_sort(data))

    print(SortAlgorithm.bubble_sort(data))

    my = SortAlgorithm(data)
    my.quicksort(0, 5)
    print(my.sort_data)
