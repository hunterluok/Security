

import time


def get_time(func):
    def wrap(x):
        start = time.time()
        result = func(x)
        usetime = time.time() - start
        print("{} use time is {}".format(func.__name__, usetime))
        return result
    return wrap


# @get_time
def f(x):
    if not isinstance(x, int):
        raise TypeError("x's type must be int")
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if x >= 2:
        return f(x-1) + f(x-2)


# @get_time
def nf(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if x >= 2:
        result = 0
        first = nf(0)
        second = nf(1)
        n = 2
        while n <= x:
            result = first + second
            n += 1
            first = second
            second = result
        return result


if __name__ == "__main__":
    # print(f(2))
    start = time.time()
    print(f(30))
    print(" {} use time is {}".format(f.__name__, time.time() - start))

    start = time.time()
    print(nf(30))
    print(" {} use time is {}".format(nf.__name__, time.time() - start))

