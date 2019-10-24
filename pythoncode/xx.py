
class Solution:
    def maxProfit(self, k: int, prices) -> int:
        lens = len(prices)
        if lens < 2:
            return 0
        a = prices

        mymins = []
        mymaxs = []
        i = 0
        j = 1
        while j < len(a):
            if a[j - 1] > a[j]:
                temp_sum = a[j - 1] - a[i]
                if temp_sum > 0:
                    mymins.append(a[i])
                    mymaxs.append(a[j - 1])
                i = j
                j += 1
            else:
                j += 1
        temp_sum = a[j - 1] - a[i]
        if temp_sum > 0:
            mymins.append(a[i])
            mymaxs.append(a[j - 1])
        mydiff = [i - j for i, j in zip(mymaxs, mymins)]

        if k >= len(mymaxs):
            last = sum(mydiff)
            return last
        if k < 1:
            return 0

        while len(mydiff) != k:
            lens = len(mydiff)
            least_index_list = [i for i in range(lens) if mydiff[i] == min(mydiff)]

            my_sums = -99
            temp_min = None
            temp_max = None

            for least_index in least_index_list:
                diff = mydiff[:]
                maxs = mymaxs[:]
                mins = mymins[:]

                after = min(lens - 1, least_index + 1)
                befor = max(0, least_index - 1)

                temp_diff_after = maxs[after] - mins[least_index]
                temp_diff_befor = maxs[least_index] - mins[befor]

                if temp_diff_befor + diff[after] > temp_diff_after + diff[befor] and temp_diff_befor > diff[befor]:
                    # 前向合并
                    maxs[befor] = maxs[least_index]
                elif temp_diff_after + diff[befor] > temp_diff_befor + diff[after] and temp_diff_after > diff[after]:
                    # 后向合并
                    mins[after] = mins[least_index]
                else:
                    pass
                mins = mins[: befor+1] + mins[after+1:]
                maxs = maxs[: befor+1] + maxs[after+1:]
                diff = [i - j for i, j in zip(maxs, mins)]

                if sum(diff) > my_sums:
                    my_sums = sum(diff)
                    temp_min = mins[:]
                    temp_max = maxs[:]

            mymins = temp_min[:]
            mymaxs = temp_max[:]
            mydiff = [i - j for i, j in zip(mymaxs, mymins)]
            print(mymaxs, mymins)
        return sum(mydiff)

if __name__ == "__main__":
    #d = [3, 5, 3, 4, 1, 4, 5, 0, 7, 8, 5, 6, 9, 4, 1]
    #d = [1, 5, 0, 8, 5, 9]
    d = [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]
    # d = [3, 5, 3, 4, 1, 4, 5, 0, 7, 8, 5, 6, 9, 4, 1]
    print(Solution().maxProfit(2, d))