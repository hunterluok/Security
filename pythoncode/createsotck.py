class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if k < 1:
            return 0
        if len(prices) < 2:
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
            return sum(mydiff)

        while len(mymaxs) != k:
            lens = len(mymaxs)
            least_index_list = [i for i in range(lens) if mydiff[i] == min(mydiff)]

            temp_maxs = None
            temp_mins = None
            temp_diff = None
            sums = 0

            for least_index in least_index_list:
                maxs = mymaxs[:]
                mins = mymins[:]
                diff = mydiff[:]
                if least_index == 0:
                    temp_diff_a = maxs[least_index + 1] - mins[least_index]
                    if temp_diff_a > diff[least_index + 1]:
                        mins[least_index + 1] = mins[least_index]
                    maxs = maxs[1:]
                    mins = mins[1:]
                    diff = [i - j for i, j in zip(maxs, mins)]
                    if sum(diff) > sums:
                        sums = sum(diff)
                        temp_maxs = maxs[:]
                        temp_mins = mins[:]
                        temp_diff = diff[:]
                elif least_index == lens - 1:
                    temp_diff_a = maxs[least_index] - mins[least_index - 1]
                    if temp_diff_a > diff[least_index - 1]:
                        maxs[least_index - 1] = maxs[least_index]
                    maxs = maxs[:-1]
                    mins = mins[:-1]
                    diff = [i - j for i, j in zip(maxs, mins)]
                    if sum(diff) > sums:
                        sums = sum(diff)
                        temp_maxs = maxs[:]
                        temp_mins = mins[:]
                        temp_diff = diff[:]
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
                    if sum(diff) > sums:
                        sums = sum(diff)
                        temp_maxs = maxs[:]
                        temp_mins = mins[:]
                        temp_diff = diff[:]
            mydiff = temp_diff[:]
            mymins = temp_mins[:]
            mymaxs = temp_maxs[:]
        return sum(mydiff)

if __name__ == "__main__":
    #2
    data = [5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]
    my = Solution()
    print(my.maxProfit(2, data))