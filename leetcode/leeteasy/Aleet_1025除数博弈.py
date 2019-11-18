

class Divide:
    def solution(self, data):
        resul = {}
        if data < 1:
            return False

        resul[1] = False
        resul[2] = True

        if data > 2:
            for i in range(3, data + 1):
                resul[i] = False
                for j in range(1, i):
                    if i % j == 0 and resul[i-j] == False:
                        resul[i] = True
                        break
                # enumerate
        return resul[data]


if __name__ == "__main__":
    my = Divide()
    s = my.solution(4)
    print(s)