


import sys

while True:
    try:
        m = int(sys.stdin.readline())
        data = {}
        for i in range(m):
            line = sys.stdin.readline()
            k, v = line.split()
            k = int(k)
            v = int(v)
            data.setdefault(k, 0)
            data[k] += v
        data = sorted(data.items(), key=lambda row: row[0])
        for line in data:
            print(str(line[0]), str(line[1]))
    except:
        break