

class Solution:
    def find(self, data, k):
        lens = len(data)
        if lens < k:
            return 0

        result = []

        for i in range(lens - 1 - k):
            temp_index = k
            temp = data[i: i + temp_index]
            temp_set = set(temp)
            while len(temp_set) != temp:
                temp += [data[temp_index]]
                temp_index += 1
            result.append(temp)
