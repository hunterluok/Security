

class Solution:
    def find(self, N, A, B):
        temp = [0] * (N + 1)

        flaga = A
        flagb = B

        change = '0'

        n = 1
        while n < N+1:
            print(temp)
            if A <= B:
                if A <= temp[n-1]:
                    temp[n] = A + flaga
                else:
                    temp[n] = A
                A += flaga
                change = 'a'
                print('a')
            else:
                if B <= temp[n-1]:
                    temp[n] = B + flagb
                else:
                    temp[n] = B
                B += flagb
                change = 'b'
                print("b")
            print("last", temp)
            n += 1
        return temp[N]


if __name__ == "__main__":
    N = 5
    A = 2
    B = 4
    my = Solution()
    print(my.find(N, A, B))




