
class Solution:
    def smallestRangeI(self, A, K: int) -> int:
        mins = min(A)
        maxs = max(A)
        if maxs - K <= mins + K:
            return 0
        else:
            return maxs - K - mins - K
