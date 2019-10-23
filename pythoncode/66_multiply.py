

class Multi:
    def solution(self, data):
        lens = len(data)
        new = [1] * lens

        for i in range(1, lens):
            new[i] = new[i-1] * data[i-1]

        temp = 1
        for i in range(lens-2, -1, -1):
            temp *= data[i+1]
            new[i] *= temp
        return new


if __name__ == "__main__":
    my = Multi()
    data = [1, 2, 3, 4, 5]
    print(my.solution(data))
