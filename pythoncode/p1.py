class Solution:
    def maxProfit(self, k: int, prices) -> int:
        lens = len(prices)
        if lens < 2:
            return 0
        a = prices

        mins = []
        maxs = []
        i = 0
        j = 1
        while j < len(a):
            if a[j - 1] > a[j]:
                temp_sum = a[j - 1] - a[i]
                if temp_sum > 0:
                    mins.append(a[i])
                    maxs.append(a[j - 1])

                i = j
                j += 1
            else:
                j += 1
        temp_sum = a[j - 1] - a[i]
        if temp_sum > 0:
            mins.append(a[i])
            maxs.append(a[j - 1])

        diff = [i - j for i, j in zip(maxs, mins)]

        if k >= len(maxs):
            last = sum(diff)
            return last
        if k < 1:
            return 0

        while len(maxs) != k:
            lens = len(diff)
            least_index = diff.index(min(diff))
            if least_index == 0:
                temp_diff = maxs[least_index + 1] - mins[least_index]
                if temp_diff > diff[least_index + 1]:
                    mins[least_index + 1] = mins[least_index]
                maxs = maxs[1:]
                mins = mins[1:]
                diff = [i - j for i, j in zip(maxs, mins)]
            elif least_index == lens - 1:
                temp_diff = maxs[least_index] - mins[least_index - 1]
                if temp_diff > diff[least_index - 1]:
                    maxs[least_index - 1] = maxs[least_index]
                maxs = maxs[:-1]
                mins = mins[:-1]
                diff = [i - j for i, j in zip(maxs, mins)]
            else:
                temp_diff_after = maxs[least_index + 1] - mins[least_index]
                temp_diff_befor = maxs[least_index] - mins[least_index - 1]

                if temp_diff_befor + diff[least_index + 1] > temp_diff_after + diff[
                            least_index - 1] and temp_diff_befor > diff[least_index - 1]:
                    maxs[least_index - 1] = maxs[least_index]
                elif temp_diff_after + diff[least_index - 1] > temp_diff_befor + diff[
                            least_index + 1] and temp_diff_after > diff[least_index + 1]:
                    mins[least_index + 1] = mins[least_index]
                else:
                    pass
                maxs = maxs[: least_index] + maxs[least_index + 1:]
                mins = mins[: least_index] + mins[least_index + 1:]
                diff = [i - j for i, j in zip(maxs, mins)]
        return sum(diff)


d = [1, 4, 2, 7, 4, 9]
print(Solution().maxProfit(1, d))