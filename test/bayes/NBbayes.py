

import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from test.logs.Alog import MyLogs


class MyBayes:
    __version__ = "1.0"

    def __init__(self, alpha=1, norm=True, prior_fit=True, laplac=None):
        self.alpha = alpha
        self.norm = norm
        self.prior_fit = prior_fit
        self.laplac = laplac
        self.mylog = MyLogs("mybayes")

    @property
    def best_score_(self):
        return self.score

    @property
    def best_estimator_(self):
        return self

    def fit(self, data, label):
        train_x, test_x, train_y, test_y = train_test_split(data, label, test_size=0.2)
        pred = self.__fit(train_x, train_y).predict(test_x)
        self.score = accuracy_score(test_y, pred)
        #return score
        return self

    def __fit(self, data, label):
        n_class = len(np.unique(label))
        m, n = data.shape

        if self.laplac is None:
            self.laplac = m

        self.mylog.info("label is {}".format(label))
        label = OneHotEncoder(categories='auto').fit_transform(label[:, np.newaxis]).toarray()

        all_count_col = np.sum(data, axis=0)
        sub_count = np.dot(label.T, data)
        self.__likelihood = (sub_count + self.alpha) / (all_count_col + self.laplac * self.alpha)

        if self.norm:
            sums = np.sqrt(np.sum(np.power(self.__likelihood, 2), axis=1, keepdims=True))
            assert sums.shape[1] == 1, "sums shape[1] != 1"
            self.__likelihood /= sums

        if not self.prior_fit:
            self.prior = np.full(n_class, 1/(n_class * 1.0))[:, np.newaxis]
        else:
            self.prior = np.sum(sub_count, axis=1, keepdims=True) / np.sum(all_count_col)
        return self

    def predict(self, testdata):
        w = np.log(self.__likelihood)
        b = np.log(self.prior)
        result = np.dot(testdata, w.T) + b.T
        pred = np.argmax(result, axis=1)
        return pred

    def get_w(self):
        return self.__likelihood


def myplot(label):
    plt.scatter(data[label == 0, 0], data[label == 0, 1])
    plt.scatter(data[label == 1, 0], data[label == 1, 1])
    plt.show()
    # count = 0
    # for i in range(3):
    #     for j in range(i+1, 4):
    #         plt.scatter(data[label == 0, i], data[label == 0, j])
    #         plt.scatter(data[label == 1, i], data[label == 1, j])
    #         count += 1
    #         print("count is {}".format(count))
    #         plt.show()
#
#
# if __name__ == "__main__":
#     from sklearn.datasets import load_iris
#     import matplotlib.pyplot as plt
#
#     data = load_iris()['data']
#     label = load_iris()['target']
#     data = load_iris()['data'][:100]
#     label = load_iris()['target'][:100]
#
#     print("---" * 20)
#     model = MyBayes(norm=False, alpha=1)
#     model.fit(data, label)
#     score = model.best_score_
#     print("score is {}".format(score))
#     print(model.get_w())
#     print(model.prior)
#
#     print("---" * 20)
#     model = MyBayes(norm=True, alpha=1, prior_fit=False)
#     model.fit(data, label)
#     score = model.best_score_
#     print("score is {}".format(score))
#     print(model.get_w())
#     print(model.prior)
#     #
#
#     print("---" * 20)
#     model = MyBayes(norm=True, alpha=1, laplac=100)
#     model.fit(data, label)
#     score = model.best_score_
#     print("score is {}".format(score))
#     print(model.get_w())
#     print(model.prior)


class GetData:
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


class NBayes:
    def __init__(self):
        self.param = {}
        self.complement = False
        self.mylog = MyLogs(self.__class__.__name__)

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

    @property
    def parameter(self):
        return self.param


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
            pri = 0.333
            # 相当于 模型的参数，2个参数？
            # pri = sub_count / all_count
            like_vect = (np.sum(sub_data, axis=0) + self.a) / (sub_count + n * self.a)
            # like_vect = (np.sum(sub_data, axis=0) + self.a) / (sub_count + 2)
            self.param.setdefault(k_label, {})
            self.param[k_label]['pri{}'.format(k_label)] = pri
            self.param[k_label]['like{}'.format(k_label)] = like_vect
        self.mylog.info(" likelihood is {}".format(self.param))
        return self


class BeNB(NBayes):
    def __init__(self, a=1):
        super(BeNB, self).__init__()
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
        self.eps = 10e-4
        self.complement = False
        self.param = {}

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


if __name__ == "__main__":
    new_data, new_label, data, label = GetData.get_testdata()

    new_data, new_label = data, label

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

    # print("xxxber"*10)
    # newmodel = BeNB()
    # preds = newmodel.fit(np.array(new_data), new_label).predict(np.array(new_data))
    # print(accuracy_score(new_label, preds))

    print("-" * 20)
    gsmode = GsNB()
    # preds = gsmode.fit(np.array(new_data), new_label).predict(np.array(new_data))
    # print(accuracy_score(new_label, preds))
    # print(gsmode.parameter)
    preds = gsmode.fit(data, label).predict(data)
    print(accuracy_score(label, preds))
    print(gsmode.parameter)
    #
    # print("--" * 15)
    # gs = GaussianNB()
    # reult = gs.fit(data, label)
    # pred_gs = gs.predict(data)
    # print(accuracy_score(label, pred_gs))
    #
    # print(gs.theta_)

