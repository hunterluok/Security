
import sys


# for line in sys.stdin:
def fss(line):
    s = ''
    if line < 2:
        print(' ')
    while line > 1:
        if line % 2 == 0:
            line //= 2
            s += str(2) + ' '
        elif line % 3 == 0:
            line //= 3
            s += str(3) + ' '
        else:
            s += str(line) + ' '
            break
    return s



import sys


#for line in sys.stdin:
def f(line):
    s = ''
    if line < 2:
        print(' ')
    while line > 1:
        if line % 2 == 0:
            line //= 2
            s += str(2) + ' '
        elif line % 3 == 0:
            line //= 3
            s += str(3) + ' '
        else:
            s += str(line) + ' '
            break
    return s


def fs(data):
    i = 2
    temp = []
    while i <= pow(data, 0.5):
        if data % i == 0:
            temp.append(i)
            data //= i
        else:
            i += 1
    if len(temp) == 0:
        return data
    else:
        temp.append(data)
    return temp

#data = sys.stdin.readline()
data = 180
print(fs(data))

