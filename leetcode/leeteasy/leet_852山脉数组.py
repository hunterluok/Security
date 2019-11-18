class Solution:
    def peakIndexInMountainArray(self, A) -> int:
        start = 0
        lens = len(A)
        for j in range(1, lens):
            if A[j] > A[start]:
                start = j
            else:
                return start