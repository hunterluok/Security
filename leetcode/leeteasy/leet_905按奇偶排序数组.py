class Solution:
    def sortArrayByParity(self, A):
        lens = len(A)
        start = 0
        end = lens - 1
        while start < end:
            while A[start] % 2 ==0 and end > start:
                start += 1
            while A[end] % 2 == 1 and end > start:
                end -= 1
            if end > start:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        return A
