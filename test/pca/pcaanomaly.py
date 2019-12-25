"""
判断异常值的 原则
（1）训练数据中没有异常点，则训练模型中的重构误差值最大的 就是临界点
（2）有少量标记样本的，以覆盖 尽可能多的标记点的值 为临界点
（3）
"""

import numpy as np
import pandas as pd
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class PCAmodel:
    def __init__(self, n_comp=None, front_m=2, front_n=2, threshold=0.95):
        self.n_comp = n_comp
        self.front_m = front_m
        self.front_n = front_n
        self.threshold = threshold

    def train(self, train_data):
        m, n = train_data.shape
        if self.n_comp is None:
            self.n_comp = n
        if self.front_m + self.front_n < self.n_comp:
            self.front_m = 1
            self.front_n = 1

        self.pcamodel = PCA(n_components=self.n_comp)
        pcadata = self.pcamodel.fit_transform(train_data)
        self.lambdas = self.pcamodel.singular_values_
        judge_matrix = np.power(pcadata, 2) / self.lambdas

        major = judge_matrix[:, 0:self.front_m]
        major = np.sum(major, axis=1, keepdims=True)
        minor = judge_matrix[:, -self.front_n:]
        minor = np.sum(minor, axis=1, keepdims=True)
        result = pd.DataFrame(np.concatenate([major, minor], axis=1), columns=['major', 'minor'])
        self.c1 = result.quantile(self.threshold)['major']
        self.c2 = result.quantile(self.threshold)['minor']
        return self

    def predict(self, testdata):
        test_pcadata = self.pcamodel.fit_transform(testdata)
        test_judgematrix = np.power(test_pcadata, 2) / self.lambdas

        major = test_judgematrix[:, 0:self.front_m]
        major = np.sum(major, axis=1, keepdims=True)
        minor = test_judgematrix[:, -self.front_n:]
        minor = np.sum(minor, axis=1, keepdims=True)
        predict_result = []
        for big, small in zip(major, minor):
            if big > self.c1 or small > self.c2:
                predict_result.append(1)
            else:
                predict_result.append(0)
        return predict_result

    @property
    def singuler(self):
        return self.lambdas

    @property
    def big_threshold(self):
        return self.c1

    @property
    def small_threshold(self):
        return self.c2


class PCAKM:
    """
    适用于较低维度的数据, 利用pca对数据进行降维处理。
     然后画图，分析聚类的数量，然后聚类（类别数量最少的就是异常点）。
    """
    def __init__(self, n_comp=0.85):
        self.n_comp = n_comp

    def train_pca(self, data):
        pcamodel = PCA(n_components=self.n_comp)
        pcadata = pcamodel.fit_transform(data)
        return pcadata

    def train_km(self, data, k=4):
        kmmodel = KMeans(n_clusters=k)
        pcadata = self.train_pca(data)
        result = kmmodel.fit_transform(pcadata)
        labels = kmmodel.labels_
        return labels


if __name__ == "__main__":
    data = load_iris()['data']
    label = load_iris()['target']

    err = np.array([[10, 3.5, 1.7, 0.21], [4.9, 3.3, 2.6, 0.9], [5.0, 8, 1.4, 0.2], [5, 3.4, 1.42, 3]])
    err_label = [-1, -1, -1, -1]
    label = np.array(label.tolist() + err_label)
    data = np.concatenate([data, err], axis=0)

    my = PCAmodel()
    result = my.train(data).predict(err)
    print(result)
    print("*"*10)

    my2 = PCAKM(n_comp=2)
    print(my2.train_km(data))
    pcadata = my2.train_pca(data)

    print(label)
    for i in [0, 1, 2, -1]:
        plt.scatter(pcadata[label == i, 0], pcadata[label == i, 1])
    plt.show()

