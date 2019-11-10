

class Solution:
    def subarraysWithKDistinct(self, A, K) -> int:
        lens = len(A)
        count = 0

        start = 0
        end = K + start

        temp = set(A[start: end])
        while len(temp) < K:

            count += 1

        for index in range(end, lens):
            pass


        print(count)
        return count




from leetcode.data import data

data = [1, 2, 3, 2]

if __name__ == "__main__":
    import cProfile
    my = Solution()
    cProfile.run("my.subarraysWithKDistinct(data, 2)", "prof.txt")
    import pstats
    p = pstats.Stats("prof.txt")
    p.sort_stats("time").print_stats()
