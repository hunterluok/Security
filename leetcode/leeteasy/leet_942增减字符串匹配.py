class Solution:
    def diStringMatch(self, S: str):
        lens = len(S)
        if lens < 1:
            return None

        new = []
        first = 0
        ends = lens
        for i in S:
            if i == 'I':
                new.append(first)
                first += 1
            else:
                new.append(ends)
                ends -= 1
        new.append(first)
        return new


