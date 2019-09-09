

def f(n):
    if n < 0:
        return "wrong"
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 2
    if n == 4:
        # f(3) + f(2)
        return 3
    if n == 5:
        return 4
    if n == 6:
        return 5
    if n == 7:
        # res = f(6) + f(5) + f(2)
        return 5
    if n == 8:
        # res = f(7) + f(6) + f(3)
        return 44
    if n == 9:
        # res = f(8) + f(7) + f(4)
        return 75
    if n == 10:
        # result = f(9) + f(8) + f(5) + f(0)
        return 129
    """
    if n == 11:
        res = f(10) + f(9) + f(6) + f(1)
        # // 220
        return res
    if n >= 12:
        result = f(n-1) + f(n-2) + f(n-5) + f(n-10)
        return result
    """

    if n >= 11:
        # 12 = 377
        no_1 = f(1)
        no_2 = f(2)
        no_3 = f(3)
        no_4 = f(4)
        no_5 = f(5)
        no_6 = f(6)
        no_7 = f(7)
        no_8 = f(8)
        no_9 = f(9)
        no_10 = f(10)


        idex = 11
        result = 0
        while idex <= n:
            idex += 1
            result = no_10 + no_9 + no_6 + no_1
            no_1 = no_2
            no_2 = no_3
            no_3 = no_4
            no_4 = no_5
            no_5 = no_5
            no_6 = no_7
            no_7 = no_8
            no_8 = no_9
            no_9 = no_10
            no_10 = result

        return result
    #"""
    # 13, 644, 1101(14), 1883(15), 3219(16)


def count_money(n):
    result = 0
    m = n + 1
    for i in range(m):
        for j in range(int(m / 2) + 1):
            for a in range(int(m / 5) + 1):
                for b in range(int(m / 10) + 1):
                    if n == i + 2 * j + 5 * a + 10 * b:
                        result += 1

    return result



if __name__ == "__main__":
    # print(f(16))
    print(count_money(7))