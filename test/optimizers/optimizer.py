

import numpy as np
from sklearn.metrics import r2_score


class Base:
    def __init__(self,
                 iters=400,
                 lr=0.0001,
                 epis=0.001):
        self.iters = iters
        self.lr = lr
        self.epis = epis
        self.w = None

    def predict(self, x, y=None):
        pred = np.dot(x, self.w)
        if y is not None:
            print(r2_score(y, pred.flatten()))
        return pred


class Reg_moment(Base):
    def __init__(self,
                 m=0.9,
                 nesterov=True):
        super().__init__()
        self.m_moment = m
        self.nesterov = nesterov

    def fit(self, x, y):
        w = np.random.randn(x.shape[1], 1)
        moment = np.zeros(w.shape)
        for _ in range(self.iters):
            for line, y_label in zip(x, y):
                error = np.dot(line.T, w) - y_label
                g = np.dot(line[:, np.newaxis], error)[:, np.newaxis]

                moment = self.m_moment * moment - self.lr * g
                if self.nesterov:
                    w += self.m_moment * moment - self.lr * g
                else:
                    w += moment
        self.w = w
        self.moment = moment
        return self


class Reg_rmsprop(Base):
    def __init__(self,
                 m_moment=0.9):
        super(Reg_rmsprop, self).__init__()
        self.m_moment = m_moment

    def fit(self, x, y):
        w = np.random.randn(x.shape[1], 1)
        moment = np.zeros(w.shape)
        for _ in range(self.iters):
            for line, y_label in zip(x, y):
                error = np.dot(line.T, w) - y_label
                g = np.dot(line[:, np.newaxis], error)[:, np.newaxis]

                moment = self.m_moment * moment + (1 - self.m_moment) * np.power(g, 2)
                w -= self.lr * g / (np.sqrt(moment) + self.epis)
        self.w = w
        self.moment = moment
        return self


class Reg_adagrad(Base):
    def __init__(self):
        super(Reg_adagrad, self).__init__()

    def fit(self, x, y):
        w = np.random.randn(x.shape[1], 1)
        moment = np.zeros(w.shape)
        for _ in range(self.iters):
            for line, y_label in zip(x, y):
                error = np.dot(line.T, w) - y_label
                g = np.dot(line[:, np.newaxis], error)[:, np.newaxis]

                moment = moment + np.power(g, 2)
                w -= self.lr * g / (np.sqrt(moment) + self.epis)
        self.w = w
        self.moment = moment
        return self


class Reg_adadelta(Base):
    def __init__(self,
                 m_moment=0.95,
                 iters=100):
        super(Reg_adadelta, self).__init__()
        self.m_moment = m_moment
        self.iters = iters

    def fit(self, x, y):
        w = np.random.randn(x.shape[1], 1)
        moment = np.zeros(w.shape)
        moment_delta = np.zeros(w.shape)
        for _ in range(self.iters):
            for line, y_label in zip(x, y):
                error = np.dot(line.T, w) - y_label
                g = np.dot(line[:, np.newaxis], error)[:, np.newaxis]

                moment = self.m_moment * moment + (1 - self.m_moment) * np.power(g, 2)
                update = g * np.sqrt(moment_delta + self.epis) / np.sqrt(moment + self.epis)
                # print("moment {}, update {}".format(moment, update))
                w -= self.lr * update
                moment_delta = self.m_moment * moment_delta + (1 - self.m_moment) * np.power(update, 2)
        self.w = w
        self.moment = moment
        self.moment_delta = moment_delta
        return self


class Reg_adam(Base):
    def __init__(self,
                 m_moment=0.95,
                 iters=100,
                 amsgrad=True):
        super(Reg_adam, self).__init__()
        self.m_moment = m_moment
        self.iters = iters
        self.beta1 = 0.9
        self.beta2 = 0.999
        self.amsgrad = amsgrad

    def fit(self, x, y):
        w = np.random.randn(x.shape[1], 1)
        ms = np.zeros(w.shape)
        mv = np.zeros(w.shape)
        if self.amsgrad:
            vhats = np.zeros(w.shape)
        else:
            vhats = np.zeros(1)

        for idex in range(self.iters):
            p_lr = self.lr * (np.sqrt(1 - np.power(self.beta2, idex + 1))) / (
            np.sqrt(1 - np.power(self.beta1, idex + 1)))
            for line, y_label in zip(x, y):
                # 计算梯度
                error = np.dot(line.T, w) - y_label
                g = np.dot(line[:, np.newaxis], error)[:, np.newaxis]

                ms = self.beta1 * ms + (1 - self.beta1) * g
                mv = self.beta2 * mv + (1 - self.beta2) * np.power(g, 2)

                if self.amsgrad:
                    vhats = np.maximum(vhats, mv)
                    w -= p_lr * ms / (np.sqrt(vhats) + self.epis)
                else:
                    w -= p_lr * ms / (np.sqrt(mv) + self.epis)
                    # print("moment {}, update {}".format(moment, update))
        self.w = w
        return self


class Reg_adamax(Base):
    def __init__(self,
                 m_moment=0.95,
                 iters=400):
        super(Reg_adamax, self).__init__()
        self.m_moment = m_moment
        self.iters = iters
        self.beta1 = 0.9
        self.beta2 = 0.999

    def fit(self, x, y):
        w = np.random.randn(x.shape[1], 1)
        ms = np.zeros(w.shape)
        us = np.zeros(w.shape)

        for idex in range(self.iters):
            p_lr = self.lr / (np.sqrt(1 - np.power(self.beta2, idex + 1)))
            for line, y_label in zip(x, y):
                # 计算梯度
                error = np.dot(line.T, w) - y_label
                g = np.dot(line[:, np.newaxis], error)[:, np.newaxis]

                ms = self.beta1 * ms + (1 - self.beta1) * g
                us = np.maximum(self.beta2 * us, np.abs(g))
                w -= p_lr * ms / (np.sqrt(us) + self.epis)
                # print("moment {}, update {}".format(moment, update))
        self.w = w
        return self


class Reg_nadam(Base):
    def __init__(self,
                 m_moment=0.004,
                 iters=400,
                 m_schedule=1,
                 beta1=0.9,
                 beta2=0.999):
        super(Reg_nadam, self).__init__()
        self.schedule_decay = m_moment
        self.m_schedule = m_schedule
        self.iters = iters
        self.beta1 = beta1
        self.beta2 = beta2

    def fit(self, x, y):
        w = np.random.randn(x.shape[1], 1)
        ms = np.zeros(w.shape)
        vs = np.zeros(w.shape)

        for idex in range(1, self.iters + 1):
            # p_lr = self.lr / (np.sqrt(1 - np.power(self.beta2, idex)))
            moment_cache_t = self.beta1 * (1.0 - 0.5 * (
                np.power(0.96, idex * self.schedule_decay)))
            moment_cache_t_1 = self.beta1 * (1.0 - 0.5 * (
                np.power(0.96, (idex + 1) * self.schedule_decay)))

            m_schedule_new = self.m_schedule * moment_cache_t
            m_schedule_next = self.m_schedule * moment_cache_t * moment_cache_t_1

            for line, y_label in zip(x, y):
                # 计算梯度
                error = np.dot(line.T, w) - y_label
                g = np.dot(line[:, np.newaxis], error)[:, np.newaxis]
                g_prime = g / (1. - m_schedule_new)
                ms = self.beta1 * ms + (1 - self.beta1) * g

                ms_prime = ms / (1. - m_schedule_next)
                vs = self.beta2 * vs + (1 - self.beta2) * np.square(g)
                vs_prime = vs / (1. - np.power(self.beta2, idex))

                ms_bar = (1. - moment_cache_t) * g_prime + moment_cache_t_1 * ms_prime
                w -= self.lr * ms_bar / (np.sqrt(vs_prime) + self.epis)
                # print("moment {}, update {}".format(moment, update))
        self.w = w
        return self


if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt

    data = load_iris()['data']
    x = data[:, 0:2]
    y = data[:, 3]
    model = LinearRegression()
    res = model.fit(x, y)
    pred = model.predict(x)
    print("scikit result r2 is {}".format(r2_score(y, pred)))

    # model = Reg_moment()
    # model = Reg_rmsprop()
    # model = Reg_adadelta()
    # model = Reg_adagrad()
    # model = Reg_adam(amsgrad=True, iters=200)
    model = Reg_adamax()
    # model = Reg_nadam()
    model.fit(x, y)
    pred = model.predict(x, y)
    plt.scatter(y, pred)
    plt.show()


