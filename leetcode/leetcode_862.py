
class Solutionss:
    def find(self, A, K):
        lens = len(A)
        if lens < 1:
            return -1

        maxs_len = float("inf")
        starts = 0
        sums = 0
        flag = False

        for ends in range(lens):
            second = A[ends]
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
                    flag = False
        if maxs_len == float("inf"):
            return -1
        return maxs_len

    def shortestSubarray(self, A, K:int) -> int:
        lens = len(A)
        if lens < 1:
            return -1
        last = float('inf')
        temp = A

        while len(temp) > 0:
            maxs_len = self.find(temp, K)
            if maxs_len != -1 and maxs_len < last:
                last = maxs_len
                print("maxs_len", maxs_len,  temp[0])
            temp = temp[1:]
        if last == float('inf'):
            return -1
        return last






if __name__ == "__main__":
    # data = [3, -1, -1, 3, -1, 3] #, -1, 3, 3]
    # # # # data = [4, 5, 6, 7, -1, 2, 4, 5, -4, 7]
    # # data = [2, -1, 2]
    # # data = [-47, 45, 92, 86, 17, -22, 77, 62, -1, 42]
    # k = 4
    data = [-30, -20, -10, 10, -50]
    # data = [-1, 2, -2, 4, -41]
    k = 5
    # data = [-28, 81, -20, 28, -29]
    # k = 89

    import time
    start = time.time()
    my = Solutionss()
    print("result ", my.shortestSubarray(data, k))
    print(time.time() - start)
