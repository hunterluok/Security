

class MergeSort:
    def mergesort(self, data):
        lens = len(data)
        step = 1
        s = 0
        while step < lens:
            i = 0
            while i < lens - (step * 2):
                s += self.sort(data, i, i + step - 1, i + step * 2 - 1)
                i += step * 2
            if i + step < lens:
                s += self.sort(data, i, i + step - 1, lens - 1)
            step *= 2
        return s

    def sort(self, data, start, mid, end):
        lens = len(data)
        if lens < 1:
            return
        new = data[:]

        right_start = mid + 1
        left_index = mid
        new_index = end
        right_index = end

        count = 0
        while left_index >= start and right_index >= right_start:
            if data[left_index] >= data[right_index]:
                new[new_index] = data[left_index]

                temp_index = right_index

                while temp_index >= right_start:
                    if data[left_index] > 2 * data[temp_index]:
                        #count += 1
                        count += temp_index - right_start + 1
                        print("ANOTH {}--{}".format(data[left_index], data[temp_index]))
                        break
                    temp_index -= 1

                new_index -= 1
                left_index -= 1
            else:
                new[new_index] = data[right_index]
                new_index -= 1
                right_index -= 1

        while left_index >= start:
            new[new_index] = data[left_index]
            left_index -= 1
            new_index -= 1
        while right_index >= right_start:
            new[new_index] = data[right_index]
            right_index -= 1
            new_index -= 1
        for i in range(start, end+1):
            data[i] = new[i]
        return count


if __name__ == "__main__":
    # data = [7, 5, 6, 4]
    # data = [1, 3, 2, 3, 1]
    # data = [2, 4, 3, 5, 1]
    #data = [-5, -5]
    data = [5, 4, 3, 2, 1]
    #data = data[::-1]
    my = MergeSort()
    #print()
    print(my.mergesort(data))
    #print(data)
    #print(my.sort(data, 0, 2, 4))
