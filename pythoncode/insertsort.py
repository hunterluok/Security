

class SortAlgorithm:
    def insert_sort(self, data):
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

    def bubble_sort(self, data):
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


if __name__ == "__main__":
    data = [6, 2, 4, 3, 7, 1]
    # data = [5, 4, 2, 1]

    print(SortAlgorithm().insert_sort(data))

    print(SortAlgorithm().bubble_sort(data))