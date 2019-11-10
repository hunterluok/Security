
class Solution:
    def maxIncreaseKeepingSkyline(self, grid) -> int:
        lens = len(grid[0])
        row_max = []
        col_max = [0] * lens
        for line in grid:
            row_max.append(max(line))
            for i in range(lens):
                if col_max[i] < line[i]:
                    col_max[i] = line[i]
        sums = 0
        for i in range(len(grid)):
            for j in range(lens):
                sums += min(row_max[i], col_max[j]) - grid[i][j]
        return sums