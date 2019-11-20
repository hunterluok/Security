class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        lens = len(deck)
        if lens < 2:
            return False
        d = {}
        for ele in deck:
            d.setdefault(ele, 0)
            d[ele] += 1
        lists = set([i for i in d.values()])
        mins = min(lists)
        if mins < 2:
            return False

        t = set()
        for i in lists:
            while i % mins != 0:
                temp = i % mins
                if temp < 2:
                    return False
                mins = temp
                i = mins
            t.add(mins)
        mins = min(t)
        for ele in t:
            if ele % mins != 0:
                return False
        return True


if __name__ == "__main__":
    d = [1, 1, 2, 2, 3, 3]
    s = Solution().hasGroupsSizeX(d)
    print(s)
