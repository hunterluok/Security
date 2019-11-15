class Solution:
    def removeDuplicates(self, nums) -> int:
        lens = len(nums)
        if lens < 2:
            return lens
        first = 0
        value = nums[first]


        i = 1
        while i < lens:
            if nums[i] > value:
                nums[first + 1], nums[i] = nums[i], nums[first + 1]
                first += 1
                #flag = first + 1
                value = nums[first]
            i += 1
        return first + 1



if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    my = Solution().removeDuplicates(data)
    print(my)
    print(data)