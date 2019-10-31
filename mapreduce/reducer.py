import sys


def outs(data):
    result = {}
    for line in data:
        k, v = line.strip().split('\t')
        result.setdefault(k, 1)
        result[k] += 1
    return result

for k, v in outs(sys.stdin).items():
    print(k, v)
