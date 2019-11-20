
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        lens = len(flowerbed)
        if lens < 1:
            return False
        elif lens == 1:
            if flowerbed[0] == 0:
                if 1 >= n:
                    return True
        count = 0
        start = 0
        alls = []
        news = 0

        if flowerbed[start] == 0:
            count += 1
            start += 1
        while start < lens and flowerbed[start] == 0 :
            count += 1
            start += 1
        if count % 2 == 0:
            news += count // 2
        else:
            news += max((count - 1) // 2, 0)

        if lens == count:
            if count % 2 == 0:
                if news >= n:
                    return True
                else:
                    return False
            else:
                news += 1
                if news >= n:
                    return True
                else:
                    return False

        count = 0
        last = lens-1
        if flowerbed[last] == 0:
            count += 1
            last -= 1
        while last>=0 and flowerbed[last] == 0:
            count += 1
            last -= 1
        if count % 2 == 0:
            news += count // 2
        else:
            news += max((count - 1) // 2, 0)

        count = 0
        for i in range(start+1, last+1):
            if flowerbed[i] == 0:
                count += 1
            else:
                alls.append(count)
                count = 0
        alls = [i for i in alls if i > 2]
        for i in alls:
            if i % 2 == 1:
                news += i // 2
            else:
                news += (i-1) // 2
        if news >= n:
            return True
        else:
            return False


if __name__ == "__main__":
    d = [0, 0, 1, 0, 1]
    d = [1, 0, 0, 0, 1]
    s = Solution().canPlaceFlowers(d, 1)
    print(s)