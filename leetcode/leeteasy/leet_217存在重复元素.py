

class Solution:
    def containsDuplicate(self, nums) -> bool:
        sets = set()
        for ele in nums:
            if ele in sets:
                return False
            else:
                sets.add(ele)
        return True

if __name__ == "__main__":
    data = [1,2 ,3,1]
    print(Solution().containsDuplicate(data))