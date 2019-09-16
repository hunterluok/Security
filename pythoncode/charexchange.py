

import numpy as np


class CharExchange:
    def __init__(self):
        pass

    def rank(self, data, start=0):
        lens = len(data)
        if start == lens-1:
            print(data, 'start {}'.format(start))
        else:
            for i in range(start, lens):
                data[start], data[i] = data[i], data[start]
                #print(data)
                self.rank(data, start=start + 1)
                data[i], data[start] = data[start], data[i]


if __name__ == "__main__":
    my = CharExchange()
    #data_or = np.array(['a', 'b', 'c','d'])
    #data = np.arange(len(data_or))
    #my.rank(data_or, data)
    data = ['a', 'b', 'c', 'd']
    my.rank(data)

