class Solution:
    """
    假设绝对存在众数
    """
    def majorityElement(self, nums) -> int:
        lens = len(nums)
        if lens < 2:
            return nums[0]
        sums = 1
        first = nums[0]
        for i in range(1, lens):
            if sums == 0:
                first = nums[i]
                sums = 1
            elif nums[i] == first:
                sums += 1
            else:
                sums -= 1
        return first