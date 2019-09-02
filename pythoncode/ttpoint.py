import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    res = {}
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        first, second = values[0], values[1]
        if first in res.keys():
            old = res[first]
            if second > old:
                res[first] == second
            else:
                continue
        else:
            res.setdefault(first, second)
    res = sorted(res.items(), key=lambda x: x[0])

    index = len(res) - 1
    result = []
    temp = 0
    while index >= 0:
        line = res[index]
        y_value = line[1]
        if y_value >= temp:
            result.append(index)
            temp = y_value
        index -= 1
    result = result[::-1]
    last_re = []
    for i in result:
        print(res[i][0], res[i][1])