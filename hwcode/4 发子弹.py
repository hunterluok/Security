

# data = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]

data = [2, 2, 2, 2, 4, 4]


def counts(data):
    count = 0
    while len(set(data)) != 1:
        if data[-1] % 2 != 0:
            data[-1] += 1
        temp = data[-1] // 2

        for i in range(len(data)):
            if data[i] % 2 != 0:
                data[i] += 1
            old = data[i]
            data[i] = temp + data[i] // 2
            temp = old // 2
        count += 1
    return count


if __name__ == "__main__":
    print(counts(data))