from sklearn.datasets import load_iris

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

import logging
import copy


# 如何 分析 聚类中心的 随着迭代次数的变化。
# 利用标记数据 分析 聚类中心点的变化。


log_format = "%(asctime)s - %(levelname)s - %(message)s"
date_format = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.INFO, filename='my.log', filemode='w', format=log_format, datefmt=date_format)


class MyKm:
    def __init__(self, k=3):
        self.k = k
        # 记录迭代的次数， count
        self.count = 0
        self.all_iter_center = []

    def caldist(self, veca, vecb):
        dist = np.sqrt(np.sum(np.power(veca - vecb, 2)))
        return np.round(dist, 2)

    def choosec(self, m):
        index = np.arange(m)
        np.random.shuffle(index)
        return index[: self.k]

    def get_centers(self, data, m):
        index_centor = self.choosec(m)
        centors = data[index_centor]
        return centors

    def __call__(self, data):
        init_loss = -np.inf
        total_loss = 0
        m = data.shape[0]
        centers = self.get_centers(data, m)
        logging.log(logging.WARNING, "init_centers are {}".format(centers))
        # 注意这个地方一定要使用 copy 这个函数。
        self.all_iter_center.append(centers.copy())

        labels = np.zeros((m, 2))
        while total_loss - init_loss > 0:
            # while self.count < 10:
            self.count += 1
            init_loss = total_loss
            for i in range(m):
                label = 0
                dist = np.Inf
                for j in range(self.k):
                    mydist = self.caldist(data[i], centers[j])
                    if mydist < dist:
                        dist = mydist
                        label = j
                labels[i, 0] = label
                labels[i, 1] = dist

            for j in range(self.k):
                temp = np.round(np.mean(data[labels[:, 0] == j], axis=0), 2)
                centers[j] = temp.tolist()
            logging.log(logging.WARNING, "init_centers are {}, at iter {}".format(centers, self.count))

            # 注意这个地方一定要使用 copy 这个函数。
            self.all_iter_center.append(centers.copy())
            # 更新 total_loss
            total_loss = np.sum(labels[:, 1])  # / m
        new_data = np.concatenate([data, labels[:, 0].reshape(m, 1)], axis=1)
        self.last_centers = centers
        return labels, new_data

    def __str__(self):
        return "total itera {}".format(str(self.count))

    @property
    def get_count(self):
        return self.count

    @property
    def center(self):
        return self.last_centers

    @property
    def get_allcener(self):
        return self.all_iter_center


class Kpp(MyKm):
    """
    Kmeans ++
    """
    def __init__(self, k):
        super(Kpp, self).__init__()
        self.k = k

    def get_centers(self, data, m):
        # 在 0~m 之间随机选择。
        first_index = np.random.randint(0, m)
        new_centers = [data[first_index].tolist()]

        logging.log(logging.INFO, "first center is {}".format(new_centers))
        k_count = 1
        # 这个地方可以优化，减少距离的计算。
        while(k_count < self.k):
            loss_contain = np.zeros(m)
            for index, line in enumerate(data):
                min_dist = np.inf
                for center in new_centers:
                    dist = self.caldist(line, center)
                    # 找到最小的距离，然后进行 后续步骤。
                    if dist < min_dist:
                        min_dist = dist
                loss_contain[index] = min_dist

            random_dist = np.random.rand() * np.sum(loss_contain)
            logging.log(logging.INFO, "random_dist is {}".format(random_dist))
            for index, dist in enumerate(loss_contain):
                random_dist -= dist
                if random_dist < 0:
                    temp_point = data[int(index)].tolist()
                    # logging.log(logging.INFO, "a new point {} no {}".format(temp_point, k_count))
                    new_centers.append(temp_point)
                    break
            k_count += 1
        logging.log(logging.WARNING, "new_centers is {}".format(new_centers))
        return new_centers


class MinShift:
    # 相当于给 中心点 周围的数据寻找新的 中心点？ 利用距离进行加权处理得到更优的结果。
    def __init__(self, h, init_err=0.5):
        self.h = h
        self.init_err = init_err

    def caldist(self, veca, vecb):
        dist = np.sqrt(np.sum(np.power(veca - vecb, 2)))
        # dist1 = np.sqrt(np.dot(veca, vecb.T), 2)
        # print(dist, dist1)
        return np.round(dist, 2)

    def calcu_kernel(self, data, line):
        m, n = data.shape
        """
        kernel = np.zeros(m)
        for index, line in enumerate(data):
            dist = self.caldist(line, x)
            kernel[index] = dist
        """
        kernel = np.sqrt(np.sum(np.power(data - line, 2), axis=1))
        # 在这几就可以控制不同的 核函数了。 相当于给样本加 权重，
        # 线性的核函数给 自身的权重最小，距离越远权重越大，这是不合适的
        kernel = (1 / (np.sqrt(2 * np.pi) * self.h)) * np.exp(-0.5 * (kernel / (self.h * self.h)))
        # 高斯 核函数 可能收敛速度 较快。 这个核函数 收敛满，kernel = np.exp(-1 * kernel)
        # 可以 给核函数。
        kernel = kernel.reshape((m, 1))
        return kernel

    def calcu_kernel_new(self, data):
        # 一个 m * m 的 矩阵
        kernel_all = []
        for line in data:
            kernel = np.sqrt(np.sum(np.power(data - line, 2), axis=1))
            kernel_all.append(kernel)
        return kernel_all

    def fit(self, data):
        new_data = []
        for line in data:
            old_vect = line
            err = np.inf
            while err > self.init_err:
                kernel = self.calcu_kernel(data, old_vect)
                mh = np.dot(kernel.T, data)
                sum_kernel = np.sum(kernel)
                mshift_vec = mh / sum_kernel
                err = self.calcu_kernel(mshift_vec, old_vect)
                old_vect = mshift_vec
            new_data.append(old_vect)
        return new_data

    @classmethod
    def get_label(cls, data):
        label = []
        for line in data:
            # 保留一位小数是一个好的选择
            temp = np.round(list(line[0]), 1)
            temp = "_".join([str(i) for i in temp])
            label.append(temp)

        result = Counter(label)
        classes = [i for i in result.keys()]
        print(classes)

        max_class = len(result)
        pred = []
        for line in label:
            for j in range(max_class):
                if line == classes[j]:
                    pred.append(j)
        return label, pred


if __name__ == "__main__":
    data = load_iris()['data']
    # label = load_iris()['target']
    # data = np.random.rand(200, 4)
    """
    mymodel = Kpp(3)
    myresult, new_data = mymodel(data)
    centers = mymodel.center
    allcenters = mymodel.get_allcener
    print(allcenters)
    print(mymodel.count)
    # ndt = pd.DataFrame(new_data, columns=['z', 'd', 'g', 'class'])
    # ndt = ndt[['d', 'z', 'g', 'class']]
    plt.scatter(data[myresult[:, 0] == 1, 0], data[myresult[:, 0] == 1, 1])
    plt.scatter(data[myresult[:, 0] == 2, 0], data[myresult[:, 0] == 2, 1])
    plt.scatter(data[myresult[:, 0] == 0, 0], data[myresult[:, 0] == 0, 1])
    #plt.scatter(centers[0][0], centers[0][1], color='black', marker="*")
    #plt.scatter(centers[1][0], centers[1][1], color='black', marker="*")
    #plt.scatter(centers[2][0], centers[2][1], color='black', marker="*")
    for center in allcenters:
        plt.scatter(center[0][0], center[0][1], color='black', marker="*")
        plt.scatter(center[1][0], center[1][1], color='black', marker="<")
        plt.scatter(center[2][0], center[2][1], color='black', marker=">")
    plt.show()
    """
    # 太大 导致没什么 聚类中心了。
    # 当 h 较大时 则 聚类的点数目，较少。 然后就是 对中心点 进行适当的保留小数位数，否则会造成中心点数量过多。
    # h的 选择 还有保留几位小数 将是一个比较难的选择。
    my = MinShift(8)
    nd = my.fit(data)
    # np.save("nd.npy", nd)
    # print(nd)
    label, pred = my.get_label(nd)
    myresult = np.array(pred).reshape(150, 1)
    plt.scatter(data[myresult[:, 0] == 1, 0], data[myresult[:, 0] == 1, 1])
    plt.scatter(data[myresult[:, 0] == 2, 0], data[myresult[:, 0] == 2, 1])
    plt.scatter(data[myresult[:, 0] == 0, 0], data[myresult[:, 0] == 0, 1])
    plt.show()

