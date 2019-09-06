

class FindMin:
    def __init__(self):
        pass

    def find_min(self, data):
        print(data)
        mins = 10000
        for i in range(len(data)):
            if data[i] < mins:
                mins = data[i]
        print("use find_min")
        return mins

    def find(self, data):
        lens = len(data)
        start = 0
        end = lens - 1
        if data[start] < data[end]:
            return data[start]

        while data[start] >= data[end]:
            mid = (end + start) // 2
            if data[start] == data[mid] and data[end] == data[mid]:
                return self.find_min(data)

            if end - start == 1:
                return data[end]

            if data[mid] >= data[end]:
                start = mid
            if data[mid] <= data[end]:
                end = mid
        #return data[end]


if __name__ == "__main__":
    test_data = [4, 5, 1, 2, 3]
    # test_data = [1, 1, 1, 0, 1]
    # test_data = [1, 1, 0, 0, 1]
    my = FindMin()
    print(my.find(test_data))

