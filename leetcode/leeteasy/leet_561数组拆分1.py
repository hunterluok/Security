

class Solution:
    def arrayPairSum(self, nums) -> int:
        d = sorted(nums)
        d = [i if idex % 2 ==0 else 0 for idex, i in enumerate(d)]
        return sum(d)


if __name__ == "__main__":
    data = [1,2,3,2]
    print(Solution().arrayPairSum(data))