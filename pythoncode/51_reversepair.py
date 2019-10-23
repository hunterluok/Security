
a = 0

class InversePair:
    def __init__(self):
        pass

    def get_pair(self, data):
        new = data[:]
        ends = len(data) - 1
        start = 0
        count = self.get_count(data, new, start, ends)
        return count

    def get_count(self, data, new, start, ends):
        if start == ends:
            new[start] = data[start]
            return 0

        length = (ends - start) // 2
        left = self.get_count(new, data, start, start+length)
        right = self.get_count(new,  data, start+length+1, ends)

        count = 0
        left_index = start + length
        right_index = ends
        new_index = ends

        while left_index >= 0 and right_index >= start + length + 1:
            if data[left_index] > data[right_index]:
                new[new_index] = data[left_index]
                count += right_index - start - length

                # print("new ", new, data)
                # p = right_index
                # while start + length + 1 <= p <= right_index:
                #     global a
                #     a += 1
                #     print(("--", data[left_index], data[p]), (a, "---a"))
                #     p -= 1

                left_index -= 1
                new_index -= 1
            else:
                new[new_index] = data[right_index]
                new_index -= 1
                right_index -= 1

        while left_index >= 0:
            new[new_index] = data[left_index]
            left_index -= 1
            new_index -= 1
        while right_index >= start + length + 1:
            new[new_index] = data[right_index]
            new_index -= 1
            right_index -= 1
        return count + left + right

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
    data = [7, 5, 6, 4]

    # data = [1, 2, 3, 4, 7, 6, 5]
    my = InversePair()
    print(my.get_pair(data))
    print(data)
    # my.test(data, 3)


