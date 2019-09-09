import numpy as np

class Corr:
    def __init__(self):
        pass

    def pearson(self, data):
        pass

    def pearson_two(self, veca, vecb):
        result = np.cov(veca, vecb) / (np.std(veca) * np.std(vecb))
        return result

    def spearman_two(self, veca, vecb):
        ranka = np.argsort(veca)
        rankb = np.argsort(vecb)
        n = len(veca)
        result = 1 - 6 * np.sum(np.power(ranka-rankb, 2))/(n * (np.power(n, 2) - 1))
        return result


if __name__ == "__main__":
    my = Corr()
    a = [1, 2, 3, 4]
    b = [2, 3, 4, 5]
    print(my.spearman_two(a, b))

