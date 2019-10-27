
class Solution:
    def find(self, data, k):
        lens = len(data)
        if lens < 1:
            return -1
        if sum(data) < k:
            return -1

        if sum(data[:-1]) < k and sum(data[1:]) < k:
            return len(data)

        left = self.find(data[:-1], k)
        right = self.find(data[1:], k)

        if left <= right and left > -1:
            return left
        if left <= right and left == -1 and right != -1:
            return right
        if right < left and right > -1:
            return right
        if right < left and right == -1 and left != -1:
            return left

if __name__ == "__main__":
    data = [1, 10, 2, -4, -3, 6, 2, 1]
    # data = [2, -1, 2]
    my = Solution()
    print(my.find(data, 9))


