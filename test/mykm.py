from sklearn.datasets import load_iris

import numpy as np
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
        while total_loss - init_loss > 0:  # 0.000000000000000001:
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


if __name__ == "__main__":
    data = load_iris()['data']
    # label = load_iris()['target']
    # data = np.random.rand(200, 4)
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

    #def plot_scatter(data=allcenters):
    for center in allcenters:
        plt.scatter(center[0][0], center[0][1], color='black', marker="*")
        plt.scatter(center[1][0], center[1][1], color='black', marker="<")
        plt.scatter(center[2][0], center[2][1], color='black', marker=">")
    # plot_scatter(allcenters)
    plt.show()

