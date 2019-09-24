

class Matrixrecon:
    def __init__(self):
        pass

    def construct(self, data):
        lens = len(data)
        mylist = [0 for _ in range(lens)]
        mylist[0] = 1

        for i in range(1, lens):
            mylist[i] = mylist[i-1] * data[i-1]

        temp = 1
        for index in range(lens-2, -1, -1):
            temp *= data[index+1]
            mylist[index] *= temp
        return mylist


if __name__ == "__main__":
    data = [3, 4, 5, 6]
    my = Matrixrecon()
    result = my.construct(data)
    print(result)

