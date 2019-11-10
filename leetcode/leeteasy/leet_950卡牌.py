

class Solution:
    def deckRevealedIncreasing(self, deck):
        dx = sorted(deck)
        lenght = len(dx)

        mid = 1
        start = -1
        data = []

        while len(dx) > 0:
            mode = mid + start
            index = mode % len(dx)
            start = index
            data.append(dx[index])
            dx.remove(dx[index])

        new = [0] * lenght
        mid = 1
        starts = -1
        my_index = []

        while lenght > 0:
            mode = mid + starts
            index = mode % lenght
            starts = index
            count = 0
            for i in range(len(new)):
                if new[i] == 0:
                    if count == index:
                        new[i] = data[0]
                        my_index.append(i)
                        break
                    count += 1
            data = data[1:]
            lenght -= 1
        temp = [0] * len(new)
        for i in range(len(new)):
            temp[i] = new[my_index.index(i)]
        return temp


if __name__ == "__main__":
    data = [17, 13, 11, 2,  3, 5, 7]
    my = Solution()
    print(my.deckRevealedIncreasing(data))

