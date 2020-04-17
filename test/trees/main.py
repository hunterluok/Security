
import numpy as np
import matplotlib.pyplot as plt


from sklearn.ensemble import GradientBoostingRegressor
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error


from test.trees.gbdt_linereg import GbLineReg, MyGbLine, MyGb_lad
from test.trees.gbdt_tree import LgbTreeLda


if __name__ == "__main__":
    # Load data
    boston = datasets.load_boston()
    X, y = shuffle(boston.data, boston.target, random_state=13)
    X = X.astype(np.float32)
    offset = int(X.shape[0] * 0.9)
    x_train, y_train = X[:offset], y[:offset]
    x_test, y_test = X[offset:], y[offset:]
    est = GradientBoostingRegressor(n_estimators=100,
                                    learning_rate=0.1,
                                    max_depth=1,
                                    random_state=0,
                                    loss='lad').fit(x_train, y_train)
    sk_pred = est.predict(x_test)
    print(mean_squared_error(y_test, sk_pred))

    # test3
    # y_train = y_train.reshape((455, 1))
    # mylr = MyGb_lad(num_iters=100, gama=0.01, beta=10000)
    # re3 = mylr.fit(x_train, y_train)
    # pr3 = mylr.predict(x_test)
    # pr3 = pr3.reshape(-1)
    # yy = y_test.reshape(-1)
    # print(mean_squared_error(yy, pr3))
    #

    # test3
    y_train = y_train.reshape((455, 1))
    mylr = LgbTreeLda()
    re3 = mylr.fit(x_train, y_train)
    pr3 = mylr.gbdt_predict(x_test)
    pr3 = pr3.reshape(-1)
    yy = y_test.reshape(-1)
    print(mean_squared_error(yy, pr3))


    # test4
    mylr = MyGbLine(num_iters=100, gama=0.01, beta=10000)
    re = mylr.fit_new(x_train, y_train)
    pr = mylr.predict(x_test)
    pr = pr.reshape(-1)
    yy = y_test.reshape(-1)
    print(mean_squared_error(yy, pr))

    plt.scatter(np.arange(51), sk_pred)
    plt.scatter(np.arange(51), pr3)
    plt.scatter(np.arange(51), pr)
    plt.scatter(np.arange(51), y_test)
    plt.legend(['sk_pred', 'gbdt_lda_pred', 'line_pred', 'real'])
    plt.show()