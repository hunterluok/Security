
import time


class Solution:
    def numDupDigitsAtMostN(self, N, start=11):
        if N < 11:
            return 0

        count = 0
        for data in range(start, N+1):
            data = str(data)
            if len(data) != len(set(data)):
                count += 1
        return count

# 18
# 10 10 - 2

# 201 - 299

# 10 + 18

if __name__ == "__main__":
    N = 299
    start = time.time()
    result = Solution().numDupDigitsAtMostN(N, start=200)
    print(result)
    print("use time {}".format(time.time() - start))