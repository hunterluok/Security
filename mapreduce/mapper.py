import sys


def main():
    for line in sys.stdin:
        line = line.strip().split(' ')
        for k in line:
            result = k + "\t" + str(1)
            yield result

for line in main():
    print(line)
