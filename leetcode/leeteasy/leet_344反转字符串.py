class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lens = len(s)
        if lens < 1:
            return None
        mid = lens // 2
        for i in range(mid):
            s[i], s[lens - i - 1] = s[lens - i - 1], s[i]