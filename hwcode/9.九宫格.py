dicts = {1: '1,.?!', 2: '2ABC', 3: '3DEF', 4: '4GHI',
         5: '5JKL', 6: '6MNO', 7: '7PQRS', 8: "8TUV", 9: "9WXYZ", 0: '0 '}
s = "22 5555 22 666 00 88 888 7777 4444 666 44"


def ggg(s):
    s = s.split()
    p = ''
    for line in s:
        lens = len(line)
        key = int(line[0])

        value = dicts[key]
        len_v = len(value)
        index = (lens - 1) % len_v
        p += value[index]
    return p


ggg(s)