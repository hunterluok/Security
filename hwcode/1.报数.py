
import numpy as np


class Bs:
    def __init__(self, start, skip):
        self.start = start
        self.skip = skip

    def fit(self, data):
        if not isinstance(data, list):
            data = list(data)

        while len(data) > 1:
            self.start = (self.start + self.skip) % len(data)
            value = data[self.start]
            # print(value)
            data.remove(value)
        print(data[0])


if __name__ == "__main__":
    data = np.arange(8)
    my = Bs(1, 2)
    my.fit(data)



