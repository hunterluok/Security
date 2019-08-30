

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

import os
import sys


# 使用绝对路径 进行处理。
parentPath = os.path.abspath("../../")
if parentPath not in sys.path:
    print(parentPath)
    sys.path.insert(0, parentPath)


class MyPCA:
    # PCA算法最主要的用途在于“降维”，去除掉数据的一些冗余信息和噪声
    # 降维使数据变得更加简单高效，从而实现提升数据处理速度的目的，
    # 数据预处理方法。高维数据集的探索与可视化.
    def __init__(self, n):
        self.n = n

    def fit(self, data):
        m, n = data.shape
        # 数据进行标准化
        means = np.mean(data, axis=0)
        stds = np.std(data, axis=0)
        datam = (data - means)/stds
        # 求解协方差矩阵
        covs = 1 / (m-1) * np.dot(datam.T, datam)
        self.eigs, eigvector = linalg.eig(covs)

        pcadata = np.dot(datam, eigvector[:, 0:self.n])
        # pcadata = pcadata * stds + means

        # 重构数据 需要与 标准差和均值一起重构。
        reconstuct = np.dot(pcadata, eigvector[0:, 0:self.n].T) * stds + means

        #ndata = np.dot(data, eigvector)
        return pcadata, reconstuct  #, ndata

    @property
    def eiglist(self):
        return self.eigs


if __name__ == "__main__":
    data = load_iris()['data']
    print(data[:4])
    mypca, recons = MyPCA(2).fit(data)
    print(mypca.shape)
    print(recons[:4])

    plt.scatter(mypca[:, 0], mypca[:, 1], color='r', marker='*')
    skpca = PCA(n_components=2).fit_transform(data)
    plt.show()

