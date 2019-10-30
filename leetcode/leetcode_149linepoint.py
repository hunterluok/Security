

class Soluntion:
    def find(self, points):
        lenss = len(points)
        if lenss < 1:
            return 0
        if lenss == 1:
            return 1

        datas = {}
        for line in points:
            temp = str(line)
            datas.setdefault(temp, 0)
            datas[temp] += 1

        del points
        list_key = [i for i in datas.keys()]
        lens = len(list_key)
        if lens == 1:
            return lenss

        result = {}

        res = {}
        for i in range(lens-1):
            for j in range(i+1, lens):
                d11 = list_key[i]
                d22 = list_key[j]

                d1 = eval(d11)
                d2 = eval(d22)

                if d2[1] == d1[1]:
                    key = str(d2[1]) + "_vetic"
                elif d2[0] == d1[0]:
                    key = str(d2[0]) + "_flag"
                else:
                    key = (d2[0] - d1[0]) / (d2[1] - d1[1])
                    b = d2[0] - key * d2[1]
                    key = str(key) + '_' + str(b)
                res.setdefault(key, []).extend([d11, d22])
                result.setdefault(key, 0)
                result[key] += 1
        result = sorted(result.items(), key=lambda s:s[1], reverse=True)
        print(result)


        #print(res[0.2], "---2222")


        res = {k: sum([datas[i] for i in set(v)]) for k, v in res.items()}
        res = sorted(res.items(), key=lambda s: s[1], reverse=True)

        print(res)
        return res[0][1]


if __name__ == "__main__":
    # data = [[1, 1], [2, 2], [1, 1], [2, 2], [1, 1], [3, 4]]

    data = [[0, -12], [5, 2], [2, 5], [0, -5], [1, 5], [2, -2], [5, -4], [3, 4], [-2, 4],
            [-1, 4], [0, -5], [0, -8], [-2, -1],[0, -11], [0, -9]]

    #data = [[0, -1], [0, 3], [0, -4], [0, -2], [0, -4], [0, 0], [0, 0], [0, 1], [0, -2], [0, 4]]
    # data = [[1,1], [1,1]]
    # data = [[1, 1], [2, 2]]
    # data =[[1,2]]
    # data = [[]]
    # data = [[0, 0], [1, 1], [1, -1], [2, -1]]
    #ata = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    my = Soluntion()
    print(my.find(data))

