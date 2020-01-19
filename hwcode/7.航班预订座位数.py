

p = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]


def get(data):
    diff = [0] * (5 + 1)
    for line in data:
        diff[line[0]-1] += line[2]
        diff[line[1]] -= line[2]
    p = diff[:]
    for i in range(5):
        p[i+1] += p[i]
    print(diff)
    print(p)
    print(sum(p[:-1]))


if __name__ == "__main__":
    get(p)