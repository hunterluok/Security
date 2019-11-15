class Solution:
    def sortedSquares(self, A):
        if len(A) < 1:
            return None

        temp_a = []
        temp_b = []
        for ele in A:
            if ele < 0:
                temp_a.append(ele ** 2)
            else:
                temp_b.append(ele ** 2)
        new = []
        lensa = len(temp_a)
        lensb = len(temp_b)

        counta = lensa
        countb = 0
        while counta > 0 and countb < lensb:
            if temp_a[counta - 1] <= temp_b[countb]:
                new.append(temp_a[counta - 1])
                counta -= 1
            else:
                new.append(temp_b[countb])
                countb += 1
        while counta > 0:
            new.append(temp_a[counta - 1])
            counta -= 1
        while countb < lensb:
            new.append(temp_b[countb])
            countb += 1
        return new
