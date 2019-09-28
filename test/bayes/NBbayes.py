

import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB


class NBayes:
    def __init__(self):
        self.param = {}
        self.complement = False

    def split_data(self, data, label, target):
        if self.complement:
            sub_data = data[label != target]
        else:
            sub_data = data[label == target]
        return sub_data

    def predict_one(self, line):
        label = None
        if self.complement:
            max_value = np.inf
        else:
            max_value = -np.inf

        for k, v in self.param.items():
            prikey = 'pri' + str(k)
            likevect = 'like' + str(k)
            ws = np.sum(np.multiply(np.log(v[likevect]), line))
            if self.complement:
                # 求最小值
                temp_pred = ws + np.log(1 - v[prikey])
                if temp_pred < max_value:
                    max_value = temp_pred
                    label = k
            else:
                # 求最大值
                temp_pred = ws + np.log(v[prikey])
                if temp_pred > max_value:
                    max_value = temp_pred
                    label = k
        return label

    def predict(self, data):
        pred = []
        for line in data:
            temp_pred = self.predict_one(line)
            pred.append(temp_pred)
        return pred

    @staticmethod
    def get_testdata():
        from sklearn.datasets import load_iris
        data = load_iris()['data']
        label = load_iris()['target']
        mean = np.mean(data, axis=0)
        new_data = []
        for line in data[:100]:
            temp = line > mean
            temp = [1 if i else 0 for i in temp]
            new_data.append(temp)
        new_label = label[:100]
        return new_data, new_label, data, label


class MultiNB(NBayes):
    def __init__(self, a=1, complement=False):
        super(MultiNB, self).__init__()
        self.a = a
        self.complement = complement

    def fit(self, data, label):
        n = len(data[0])
        n_class = np.unique(label)
        all_count = np.sum(np.sum(data))
        for k_label in n_class:
            sub_data = self.split_data(data, label, k_label)
            sub_count = np.sum(np.sum(sub_data))
            # pri = 0.5
            # 相当于 模型的参数，2个参数？
            pri = sub_count / all_count
            like_vect = (np.sum(sub_data, axis=0) + self.a) / (sub_count + n * self.a)
            # like_vect = (np.sum(sub_data, axis=0) + self.a) / (sub_count + 2)
            self.param.setdefault(k_label, {})
            self.param[k_label]['pri{}'.format(k_label)] = pri
            self.param[k_label]['like{}'.format(k_label)] = like_vect
        return self

    @property
    def parameter(self):
        return self.param


class BeNB(NBayes):
    def __init__(self, a=1):
        super(BeNB, self).__init__()
        self.param = {}
        self.a = a

    def fit(self, data, label):
        n_class = np.unique(label)
        for k_label in n_class:
            sub_data = self.split_data(data, label, k_label)
            sub_count = np.sum(np.sum(sub_data))
            pri = 0.5
            # 相当于 模型的参数，2个参数？
            like_vect = (np.sum(sub_data, axis=0) + self.a) / (sub_count + 2)
            self.param.setdefault(k_label, {})
            self.param[k_label]['pri{}'.format(k_label)] = pri
            self.param[k_label]['like{}'.format(k_label)] = like_vect
        return self

    def predict_one(self, line):
        label = None
        max_value = -np.inf
        for k, v in self.param.items():
            prikey = 'pri' + str(k)
            likevec = 'like' + str(k)
            ws = np.sum(np.multiply(np.log(v[likevec]), line))
            neg = np.sum(np.multiply((1 - v[likevec]), 1 - line))

            temp_pred = ws + np.log(v[prikey]) + neg
            if temp_pred > max_value:
                max_value = temp_pred
                label = k
        return label

class GsNB(NBayes):
    def __init__(self):
        super(GsNB).__init__()
        self.param = {}
        self.eps = 10e-4

    def fit(self, data, label):
        n_class = np.unique(label)
        m = data.shape[0]

        for k_label in n_class:
            sub_data = self.split_data(data, label, k_label)

            sub_m = sub_data.shape[0]
            sub_mean = np.mean(sub_data, axis=0)
            sub_var = np.var(sub_data, axis=0)

            self.param.setdefault(k_label, {})
            # 相当于 模型的参数，相当于三个参数？
            self.param[k_label]['pri{}'.format(k_label)] = sub_m / m
            self.param[k_label]['mean{}'.format(k_label)] = sub_mean
            self.param[k_label]['var{}'.format(k_label)] = sub_var
        return self

    def cal_gs(self, line, mean, var):
        theta = 2 * var + self.eps
        left = 1 / np.sqrt(np.pi * theta)
        right = np.exp(-1 * (1 / theta) * np.power(line-mean, 2))
        return np.multiply(left, right)

    def predict_one(self, line, complement=False):
        print("sx")
        label = None
        max_value = -np.inf
        for k, v in self.param.items():
            prikey = 'pri' + str(k)
            meankey = 'mean' + str(k)
            stdkey = 'var' + str(k)
            likevect = self.cal_gs(line, v[meankey], v[stdkey])
            temp_pred = np.sum(np.log(likevect + self.eps)) + np.log(v[prikey])
            if temp_pred > max_value:
                max_value = temp_pred
                label = k
        return label

    @property
    def parameter(self):
        return self.param


if __name__ == "__main__":
    my = NBayes()

    new_data, new_label, data, label = my.get_testdata()

    # sklearn 的算法
    muti = MultinomialNB(alpha=1)
    reult = muti.fit(new_data, new_label)
    preds = muti.predict(new_data)
    print(accuracy_score(new_label, preds))


    gs = GaussianNB()
    reult = gs.fit(new_data, new_label)
    pred_gs = gs.predict(new_data)
    print(accuracy_score(new_label, pred_gs))
    print(":" * 20)

    newmodel = MultiNB(complement=True)
    preds = newmodel.fit(np.array(new_data), new_label).predict(np.array(new_data))
    print(accuracy_score(new_label, preds))
    print(newmodel.parameter)


    print("xxx"*10)
    newmodel = MultiNB(complement=False)
    preds = newmodel.fit(np.array(new_data), new_label).predict(np.array(new_data))
    print(accuracy_score(new_label, preds))
    print(newmodel.parameter)


    print("xxxber"*10)
    newmodel = BeNB()
    preds = newmodel.fit(np.array(new_data), new_label).predict(np.array(new_data))
    print(accuracy_score(new_label, preds))


    # print("-" * 20)
    # gsmode = GsNB()
    # # preds = gsmode.fit(np.array(new_data), new_label).predict(np.array(new_data))
    # # print(accuracy_score(new_label, preds))
    # # print(gsmode.parameter)
    # preds = gsmode.fit(data, label).predict(data)
    # print(accuracy_score(label, preds))
    # print(gsmode.parameter)
    #
    # print("--" * 15)
    # gs = GaussianNB()
    # reult = gs.fit(data, label)
    # pred_gs = gs.predict(data)
    # print(accuracy_score(label, pred_gs))
    #
    # print(gs.theta_)

