class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        if right < left:
            return None
        new = []
        for temps in range(left, right + 1):
            ele = temps
            flag1 = True
            flag2 = True
            while ele > 0:
                temp = ele % 10
                if temp == 0:
                    flag1 = False
                    break
                if temps % temp != 0:
                    flag2 = False
                    break
                ele //= 10
            if flag1 and flag2:
                new.append(temps)
        return new
