

def get_profit(a, k=2):
    sums = []
    i = 0
    j = 1
    while j < len(a):
        if a[j - 1] > a[j]:
            temp_sum = a[j - 1] - a[i]
            if temp_sum > 0:
                sums.append(temp_sum)
            i = j
            j += 1
        else:
            j += 1

    temp_sum = a[j - 1] - a[i]
    if temp_sum > 0:
        sums.append(temp_sum)

    print("all {}".format(sums))
    sums = sorted(sums, reverse=True)[:k]
    print("qian k {}".format(sums))
    return sum(sums)

if __name__ == "__main__":
    d = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    res = get_profit(d, k=2)
    print(res)
