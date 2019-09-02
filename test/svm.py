
import numpy as np


class MySvm:
    def __init__(self, ):

        pass

    def get_minmax(self, value, low, high):
        if value < low:
            return low
        elif value > high:
            return high
        else:
            return value

    def fit(self, data):
        m, n = data.shape
        self.alpha = np.zeros((m, 2))
        b = 0
        pass




