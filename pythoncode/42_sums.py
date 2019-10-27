

class Solution:
    def __init__(self):
        pass

    def find(self, data):
        if len(data) < 1:
            return None

        lens = len(data)
        max_sum = -float("inf")
        temp_sum = 0
        print(max_sum, '__')
        for i in range(0, lens):
            temp_sum += data[i]
            if max_sum < temp_sum:
                max_sum = temp_sum
                print(max_sum, '__')
            if temp_sum < 0:
                temp_sum = 0
        return max_sum


if __name__ == "__main__":
    # data = [-1, 2, 1, -2, 3, 10, -4, 7, 2, -5]
    data = [-5, -2, -1, -6]
    my = Solution()
    print(my.find(data))

