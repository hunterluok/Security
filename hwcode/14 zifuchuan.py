
data = ['me', 'sds', 'meto', 'sdsd', 's']


def ys(data):
    data = sorted(data)
    lens = 0
    start = 0
    s = data[start]
    lens += len(s)
    for i in range(1, len(data)):
        if data[i].startswith(s):
            lens += len(data[i]) - len(s)
        else:
            lens += len(data[i])
        s = data[i]
    return lens


print(ys(data))