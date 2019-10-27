
class Solution:
    def find(self, data, k):
        lens = len(data)
        if lens < 1:
            return -1
        x1 = 0
        x2 = 0
        sums = 0
        starts = 0
        flag = False

        maxs_len = float("inf")

        for ends in range(lens):
            second = data[ends]
            sums += second
            if second < 0:
                flag = True
            if sums >= k:
                if sums - data[starts] >= k:
                    while sums - data[starts] >= k and starts < ends:
                        sums -= data[starts]
                        starts += 1
                # 找到了一个子数组
                print("from ", starts, " to", ends)
                print("temp lens is {}".format(ends - starts + 1))
                if maxs_len > ends - starts + 1:
                    maxs_len = ends -starts + 1
                    print(maxs_len, " maxlen")

                if flag:
                    temp_sum = sums
                    temp_index = starts
                    while temp_index <= ends:
                        if temp_sum - data[temp_index] < k:
                            temp_sum -= data[temp_index]
                            temp_index += 1
                        else:
                            # 更新 sums 和 start
                            temp_index += 1

                            sums = temp_sum - data[temp_index]
                            starts = temp_index

                            temp_len = ends - temp_index + 1
                            if temp_len < maxs_len:
                                maxs_len = temp_len
                    flag = False

        print(x1, x2, "xxx")
        if maxs_len == float("inf"):
            return -1
        return maxs_len


if __name__ == "__main__":
    data = [3, -1, -1, 3, -1, 3]
    # data = [4, 5, 6, 7, -1, 2, 4, 5, -4, 7]
    # data = [2, -1, 2, 2]
    # data = [2, -1, 2, 2]
    k = 5
    ##data = [2, -1, 2]
    my = Solution()
    print("result ", my.find(data, k))
