# utf-8

from sklearn.datasets import load_iris
import random
import numpy as np
import logging

log_format = "%(asctime)s - %(levelname)s - %(message)s"
date_format = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.INFO, filename='mysvm.log', filemode='w', format=log_format, datefmt=date_format)


class SgdSvm:
    def __init__(self, examples, maxiters, lam=1000):
        self.examples = examples
        self.maxiters = maxiters
        self.lam = lam

    def fit(self, data, label):
        m, n = data.shape
        indexs = np.arange(m)
        num_data = int(self.examples * m)
        w = np.random.randn(n, 1)
        logging.log(logging.WARNING, "init_w is {}".format(w))
        iters = 0
        while iters < self.maxiters:
            iters += 1
            random.shuffle(indexs)
            temp_data = data[:num_data]
            temp_label = label[:num_data]

            if len(temp_label.shape) != 2:
                temp_label = temp_label.reshape((-1, 1))
            # eta = 1.0 / (self.lam + iters)
            pred = np.dot(temp_data, w)
            error = np.multiply(pred, temp_label)
            # logging.log(logging.WARNING, "error's shape is {}".format(error.shape))
            # logging.log(logging.WARNING, "error's is {}".format(error))
            temp_error = error.reshape(-1)
            if len(temp_error.shape) != 1:
                logging.log(logging.ERROR, "temp error's shape is {}".format(temp_error.shape))

            logging.log(logging.INFO, "temp error's shape is {}".format(temp_error.shape))
            error_data = temp_data[temp_error < 1]
            error_label = temp_label[temp_error < 1]
            w_delta = np.dot(error_data.T, error_label)
            w = (1 - 1/iters) * w + (1 / (self.lam * num_data)) * w_delta
        self.w = w
        return w

    def predict(self, data, test_label):
        pred_old = np.dot(data, self.w)
        pred_new = [[1] if i >= 0.5 else [-1] for i in pred_old]
        acc = np.sum(pred_new == test_label.reshape((-1, 1)))
        lens = len(test_label)
        print(acc, lens)
        return acc / lens


if __name__ == "__main__":
    data = load_iris()['data']
    label = load_iris()['target']
    # print(label)
    data = data[label != 1]
    label = label[label != 1]
    label = (label-1).reshape((-1, 1))
    #label = np.array([-1 if i == 0 else 1 for i in label]).reshape((-1, 1))
    mysvm = SgdSvm(examples=0.9, maxiters=100, lam=1000)
    w = mysvm.fit(data, label)
    print(w)
    acc = mysvm.predict(data, label)
    print("mysvm's acc is {}".format(acc))

