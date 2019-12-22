
import numpy as np

from test.logs.Alog import MyLogs


class KmDist:
    def __init__(self):
        self.mylog = MyLogs(self.__class__.__name__)

    def _cal_dist(self, veca, vecb, flag='circle', T=24, ordermaxmin=(1, 0)):
        if flag == "circle":
            t1_dist = abs(veca - vecb)
            t2_dist = np.min([abs(T - vecb + veca), abs(T - veca + vecb)])
            # 注意这里的 12， 不是24，是因为小时之间的最大 距离就是12，不是24.
            dist = np.sum(np.min([t1_dist, t2_dist]) / 12)
            return dist
        elif flag == "nominal":
            dist = [1 if i == j else 0 for i, j in zip(veca, vecb)]
            return np.sum(dist)
        elif flag == "order":
            maxs = ordermaxmin[0]
            mins = ordermaxmin[1]
            if maxs == mins:
                raise ValueError("maxs must be greater than mins")
            dist = np.sum(abs(vecb - veca) / (maxs - mins))
            return dist
        elif flag == "dist":
            dist = np.sqrt(np.sum(np.power(veca - vecb, 2)))
            return dist
        else:
            raise TypeError("flag must in (circle, nominal, order, dist)")

    def cal_dist(self, va, vb, kargs=None): # needsub=True, kargs={"nominal":[0, 1]}):
        total_dist = 0

        lens = len(va)
        temp_lens = set()
        if kargs is not None and isinstance(kargs, dict):
            for key, value in kargs.items():
                sub_va = va[value]
                sub_vb = vb[value]
                dist = self._cal_dist(sub_va, sub_vb, flag=key)
                total_dist += dist
                temp_lens |= set(value)
                self.mylog.info("key is {}, dist is {}".format(key, dist))

        reserve = set(np.arange(lens)) - temp_lens
        if len(reserve) > 0:
            ids = list(reserve)
            # 注意这里 为什么不能用 isinstance((va, vb), list): 难道是至少满足一个条件么。
            if isinstance(va, list):
                va = np.array(va)
            if isinstance(vb, list):
                vb = np.array(vb)

            sub_vb = vb[ids]
            sub_va = va[ids]
            # sub_va = np.array([float(i) for i in va[ids]])
            # sub_vb = np.array([float(i) for i in vb[ids]])
            dist = self._cal_dist(sub_va, sub_vb, flag='dist')
            total_dist += dist
        return total_dist


if __name__ == "__main__":
    d1 = np.array([1, 1, 2, 1])
    d2 = np.array([1, 2, 3, 4])
    my = KmDist()

    res = my.cal_dist(d1, d2, kargs={"nominal": [0, 1], "order":[2, 3]})
    print(res)
