def get_profit(a, k=2):
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
                print("best {} - {} diff is {}".format(a[i], a[j - 1], a[j-1] - a[i]))
            i = j
            j += 1
        else:
            j += 1
    temp_sum = a[j - 1] - a[i]
    if temp_sum > 0:
        mymins.append(a[i])
        mymaxs.append(a[j - 1])
        print("best {} - {}".format(a[i], a[j - 1]))
    mydiff = [i - j for i, j in zip(mymaxs, mymins)]

    if k >= len(mymaxs):
        last = sum(mydiff)
        return last
    if k < 1:
        return 0

    while len(mymaxs) != k:
        lens = len(mymaxs)
        least_index_list = [i for i in range(lens) if mydiff[i] == min(mydiff)]

        temp_maxs = None
        temp_mins = None
        temp_diff = None
        sums = -999

        for least_index in least_index_list:
            print("88")
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
                print("left", maxs, mins)
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
                print("right", maxs, mins)
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
                print("midd", maxs, mins)
        print(temp_diff)
        mydiff = temp_diff[:]
        mymins = temp_mins[:]
        mymaxs = temp_maxs[:]
    print("last", mymaxs, mymins)
    return sum(mydiff)


if __name__ == "__main__":
    # d = [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]
    # d = [3, 5, 3, 4, 1, 4, 5, 0, 7, 8, 5, 6, 9, 4, 1]
    d = [5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]

    k = 7
    d= [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11,
     94]
    print(get_profit(d, k=8))

# 469