
class Solutionss:
    def find(self, A, K):
        lens = len(A)
        if lens < 1:
            return -1

        maxs_len = float("inf")
        starts = 0
        sums = -float("inf")
        flag = False

        for ends in range(lens):
            second = A[ends]
            if second >= sums and sums < 0:
                sums = second
                starts = ends
            else:
                sums += second

            if second < 0:
                flag = True
            if sums >= K:
                if sums - A[starts] >= K:
                    while sums - A[starts] >= K and starts < ends:
                        sums -= A[starts]
                        starts += 1
                if maxs_len > ends - starts + 1:
                    maxs_len = ends - starts + 1
                if flag:
                    temp_sum = sums
                    temp_index = starts
                    while temp_index <= ends:# and temp_index < ends:
                        if temp_sum - A[temp_index] < K:
                            temp_sum -= A[temp_index]
                            temp_index += 1
                        else:
                            temp_index += 1
                            sums = temp_sum - A[temp_index]
                            starts = temp_index
                            temp_len = ends - temp_index + 1
                            if temp_len < maxs_len:
                                maxs_len = temp_len
                    # print("s - end ", starts, ends)
                    flag = False

        if maxs_len == float("inf"):
            return -1
        return maxs_len


if __name__ == "__main__":
    # data = [3, -1, -1, 3, -1, 3] #, -1, 3, 3]
    # # # # data = [4, 5, 6, 7, -1, 2, 4, 5, -4, 7]
    data = [2, -1, 2]
    # data = [-47, 45, 92, 86, 17, -22, 77, 62, -1, 42]
    k = 3
    #data = [-30, -20, -10, 10, -50]
    # data = [-1, 2, -2, 4, -41]
    #k = 5
    # data = [-28, 81, -20, 28, -29]
    # k = 89
    data = [11, 47, 97, 35, -46, 59, 46, 51, 59, 80, 14, -6, 2, 20, 96, 1, 18, 74, -17, 71]
    k = 282

    import time
    start = time.time()
    my = Solutionss()
    print("result ", my.find(data, k))
    print(time.time() - start)
