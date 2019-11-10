class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return bin(x ^ y).count('1')
        t1 = 0
        while x != 0 and y != 0:
            if x % 2 != y % 2:
                t1 += 1
            x //= 2
            y //= 2
        while x != 0:
            if x % 2 != 0:
                t1 += 1
            x //= 2
        while y != 0:
            if y % 2 != 0:
                t1 += 1
            y //= 2
        return t1