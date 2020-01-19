
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))


import sys

ds = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
keys = set(["A", "B", "C", "D", "E", "F"])


for strs in sys.stdin:
    temp = strs.strip()[2:]
    lens = len(temp) - 1
    s = 0
    for i in temp:
        if i in keys:
            s += ds[i] * pow(16, lens)
            lens -= 1
        else:
            i = int(i)
            s += i * pow(16, lens)
            lens -=1
    print(str(s))
