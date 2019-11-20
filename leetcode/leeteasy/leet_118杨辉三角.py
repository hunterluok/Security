class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        last = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = last[i - 1]
            n_t = [1]
            for t in range(len(temp) - 1):
                n_t.append(temp[t] + temp[t + 1])
            n_t.append(1)
            last.append(n_t)
        return last
