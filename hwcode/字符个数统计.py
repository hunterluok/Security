

import sys


class CountChar:
    def countch(self, strs):
        strs = strs.strip()
        lens = len(strs)
        data = set()
        for i in range(lens):
            if 0 <= ord(strs[i]) <= 127:
                data.add(strs[i])
        return len(data)

if __name__ == "__main__":
    strs = sys.stdin.readline()
    result = CountChar().countch(strs)
    print(result)