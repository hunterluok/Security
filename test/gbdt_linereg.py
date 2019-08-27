# A test

import numpy as np
import matplotlib.pyplot as plt


from sklearn.ensemble import GradientBoostingRegressor
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error


class gb_linereg:
    def __init__(self, gama=0.1, num_iters=20):
        self.gama = gama
        self.num_iters = num_iters
        self.param_dicts = {}

    def fit(self, data, y):
        self.meany = np.mean(y)

        m, n = data.shape
        w = np.random.randn(n).reshape(n, 1)
        y0 = np.mean(y)

        gama = self.gama
        for i in range(self.num_iters):
            self.param_dicts.setdefault(i, {})
            dety = y - y0
            error = gama * np.dot(data, w) - dety
            w = w - 1 / m * np.dot((gama * data).T, error)
            gama = gama - 1 / m * np.dot((np.dot(data, w)).T, error)
            # 也可以设定档 w,  和 gama 不怎么变化时 就停止运算。
            self.param_dicts[i].setdefault("w", w)
            self.param_dicts[i].setdefault("gama", gama)
            y0 = y0 + gama * (np.dot(data, w))
        return self

    def predict(self, data):
        pred = self.meany
        for k, v in self.param_dicts.items():
            temp = np.dot(data, v['w']) * v['gama']
            pred += temp
        return pred

    def get_param(self):
        return self.param_dicts


class GbLineReg:
    def __init__(self, gama=0.1, num_iters=20, beta=10000, line_iters=100):
        self.gama = gama
        self.beta = beta
        self.num_iters = num_iters
        self.line_iters = line_iters
        self.param_dicts = {}

    def fit(self, data, y):
        m, n = data.shape
        y0 = np.mean(y)
        self.param_dicts.setdefault("init_fx", y0)
        gama = self.gama

        for i in range(self.num_iters):
            self.param_dicts.setdefault(i, {})
            # 这里更新残差的地方
            w = np.random.randn(n).reshape(n, 1)
            # 梯度下降的方式不一定可行的。
            # 利用随机梯度下降的效果略好些， 此处用的是梯度下降。
            # 梯度下降中 这个 self.beta起着很重要的作用。
            for _ in range(self.line_iters):
                dety = y - y0
                error = gama * np.dot(data, w) - dety
                w = w - (1 / (m * self.beta)) * gama * np.dot(data.T, error)
            # 也可以设定档 w,  就停止运算。
            self.param_dicts[i].setdefault("w", w)
            self.param_dicts[i].setdefault("gama", gama)
            y0 = y0 + np.dot(data, w) * gama
            # gama *= 1 / np.exp(self.num_iters)
            gama *= 0.1
        return self

    def predict(self, data):
        pred = self.param_dicts["init_fx"]
        for k, v in self.param_dicts.items():
            if k != 'init_fx':
                temp = np.dot(data, v['w']) * v['gama']
                pred += temp
        return pred

    def get_param(self):
        return self.param_dicts


class MyGbLine(GbLineReg):
    def __int__(self, beta=10000):
        super(MyGbLine, self).__init__()
        # self.beta 其实是控制了 梯度下降的稳定性，可以考虑换成其他的求解方式。
        self.beta = beta

    def fit_new(self, data, y):
        m, n = data.shape
        y0 = np.mean(y)
        self.param_dicts.setdefault("init_fx", y0)
        gama = self.gama

        for i in range(self.num_iters):
            self.param_dicts.setdefault(i, {})
            w = np.random.randn(n).reshape(n, 1)
            dety = y - y0
            for _ in range(int(self.line_iters/100)):
                for index in range(m):
                    temp_data = data[index].reshape(1, n)
                    error = np.multiply(gama, np.dot(temp_data, w)) - dety[index]
                    w = w - (1 / self.beta) * np.dot((np.multiply(gama, temp_data)).T, error)
            self.param_dicts[i].setdefault("w", w)
            self.param_dicts[i].setdefault("gama", gama)
            y0 = y0 + gama * (np.dot(data, w))
            # gama当作学习速率进行看待，而不是其他的东西。
            gama *= 1 / np.exp(self.num_iters)
        return self


if __name__ == "__main__":
    # test1
    def get_data(num=1000):
        w = np.array([[1], [2], [3]])
        b = np.random.randn(num).reshape(num, 1)
        x = np.random.rand(num, 3)
        y = np.dot(x, w) + b
        return np.round(x, 2), np.round(y, 2)

    x, y = get_data()
    mylr = gb_linereg()
    re = mylr.fit(x, y).predict(x)
    pr = mylr.predict(x)
    pr = pr.reshape(-1)
    yy = y.reshape(-1)

    # test2
    # Load data
    boston = datasets.load_boston()
    X, y = shuffle(boston.data, boston.target, random_state=13)
    X = X.astype(np.float32)
    offset = int(X.shape[0] * 0.9)
    x_train, y_train = X[:offset], y[:offset]
    x_test, y_test = X[offset:], y[offset:]
    est = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,
                                    max_depth=1, random_state=0, loss='ls').fit(x_train, y_train)
    print(mean_squared_error(y_test, est.predict(x_test)))

    # test3
    y_train = y_train.reshape((455, 1))
    mylr = GbLineReg(num_iters=100, gama=0.01, beta=10000)
    re = mylr.fit(x_train, y_train)
    pr = mylr.predict(x_test)
    pr = pr.reshape(-1)
    yy = y_test.reshape(-1)
    print(mean_squared_error(yy, pr))
    plt.scatter(np.arange(51), pr)

    # test4
    mylr = MyGbLine(num_iters=100, gama=0.01, beta=10000)
    re = mylr.fit_new(x_train, y_train)
    pr = mylr.predict(x_test)
    pr = pr.reshape(-1)
    yy = y_test.reshape(-1)
    print(mean_squared_error(yy, pr))

    plt.scatter(np.arange(51), pr)
    plt.scatter(np.arange(51), y_test)
    plt.legend(['test3_pred', 'test4_pred', 'real'])
    plt.show()

