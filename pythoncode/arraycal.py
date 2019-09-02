
import sys


def find(line):
    maxs_value = min(line) * sum(line)
    if len(line) == 1:
        return maxs_value

    mins = min(line)
    min_index = line.index(mins)
    left = line[0: min_index]
    right = line[min_index + 1:]

    if len(left) == 1:
        left_max = left[0] * left[0]
        maxs_value = max([maxs_value, left_max])
    if len(right) == 1:
        right_max = right[0] * right[0]
        maxs_value = max([maxs_value, right_max])

    if len(left) > 1:
        temp = min(left) * sum(left)
        # maxs_value = ([maxs_value, temp])
        val = find(left)
        maxs_value = max([maxs_value, val, temp])
    if len(right) > 1:
        temp = min(right) * sum(right)
        val = find(right)
        maxs_value = max([maxs_value, val, temp])
    return maxs_value


def cal(data, step=1, lens=10):
    maxs = 0
    for i in range(lens - step + 1):
        temp = data[i: i + step]
        new_max = min(temp) * sum(temp)
        if maxs < new_max:
            maxs = new_max
    return maxs


def get_max(data, n):
    maxs = 0
    for i in range(1, 1+n):
        new_max = cal(data, step=i, lens=n)
        if new_max > maxs:
            maxs = new_max
    return maxs


if __name__ == "__main__":
    # python arraycal.py < arraycal.txt
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    line = list(map(int, line.split()))
    res = find(line)
    # res = get_max(line, n) 内存消耗更大
    print(res)