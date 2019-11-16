class Solution:
    def heightChecker(self, heights) -> int:
        lens = len(heights)
        if lens < 2:
            return 0

        new = sorted(heights)
        count = 0
        for i in range(lens):
            if new[i] != heights[i]:
                count += 1
        return count


