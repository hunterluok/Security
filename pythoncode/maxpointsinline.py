
import numpy as np

class maxpoints:
    def __init__(self):
        pass

    def cal(self, data):
        lens = len(data)
        results = {}

        for i in range(lens-1):
            for j in range(i+1, lens):
                x1 = data[i][0]
                y1 = data[i][1]

                x2 = data[j][0]
                y2 = data[j][1]

                if x1 != x2:
                    k = (y1 - y2) / (x1 - x2)
                    b = y1 - k * x1
                #注意处理分母为0的情况
                else:
                    k = np.inf
                    b = x1
                key = str(k) + "_" + str(b)
                results.setdefault(key, 0)
                results[key] += 1

        results = sorted(results.items(), key=lambda s: s[1], reverse=True)
        maxcount = results[0][1]
        print(results)
        # 乘以2 以后向上取整数就可以了。
        return int(np.sqrt(maxcount * 2)) + 1


if __name__ == "__main__":
    #data = [[1, 2], [3, 4], [4, 8], [3, 4], [2, 4]]
    data = [[1, 2], [1, 4], [1, 5], [-1, 2], [-1, 4], [-1, 5]]
    my = maxpoints()
    print(my.cal(data))

