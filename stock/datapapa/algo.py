
import multiprocessing
import requests
from bs4 import BeautifulSoup
import re
import bs4
import time

import numpy as np

from stock.datapapa.all import getHistoryTradeInfo, get_name


# def judge(data):
#     temp = []
#     for line in data:
#         try:
#             temp.append(float(line[10]))
#         except:
#             pass
#             # print(line)
#     try:
#         mid = np.median(temp)
#         temp_sort = sorted(temp)
#         mid_90 = temp_sort[int(0.85 * len(temp))]
#
#         now = np.mean(temp[:2])
#         if now > mid and now < mid_90:
#             print("nice stock", data[2][2])
#             print(mid, mid_90, now)
#             return True
#     except:
#         return False
#     return False
#
#
# def get_fit_stock(keys):
#     lists = []
#     for key in keys:
#         data = getHistoryTradeInfo(key, ndays=300)
#         if data is None:
#             continue
#         else:
#             if judge(data):
#                 lists.append([key, data[2][2]])
#     return lists

class Job:
    def __init__(self,
                 n_jobs=2):
        self.n_jobs = n_jobs

    def judge(self, data):
        temp = []
        for line in data:
            try:
                temp.append(float(line[10]))
            except:
                pass
                # print(line)
        try:
            mid = np.median(temp)
            temp_sort = sorted(temp)
            mid_90 = temp_sort[int(0.85 * len(temp))]
            now = np.mean(temp[:2])
            if now > mid and now < mid_90:
                print("nice stock", data[2][2])
                print(mid, mid_90, now)
                return True
        except:
            return False
        return False

    def get_fit_stock(self, keys):
        for key in keys:
            data = getHistoryTradeInfo(key, ndays=300)
            if data is None:
                continue
            else:
                if self.judge(data):
                    print(key, data[2][2])
                    #lists.append([key, data[2][2]])
                else:
                    pass

    def split_data(self, n_jobs):
        # page_list = np.arange(1, self.n_page + 1)
        stock_code_list = get_name("allname.txt")[:10]

        indexs = int((len(stock_code_list) - 1) / n_jobs) + 1
        for id in range(n_jobs):
            temp = stock_code_list[indexs * id: (id + 1) * indexs]
            print(temp)
            yield temp

    def savedata_multiprocess(self):
        # logging.log(logging.INFO, "db infomation are {}".format(mins))
        if self.n_jobs == -1:
            # 获取 cpu的个数
            n_jobs = multiprocessing.cpu_count() - 2
        else:
            n_jobs = self.n_jobs
        print("n_jobs is {}".format(n_jobs))

        def get_mu(q, keys):
            self.get_fit_stock(keys)
            q.put(1)

        q = multiprocessing.Queue()
        myqueus = []
        sums = 0
        for ids, p_list in enumerate(self.split_data(n_jobs)):
            temp_job = multiprocessing.Process(target=get_mu, args=(q, p_list), name="jon_{}".format(ids))
            myqueus.append(temp_job)
        for job in myqueus:
            job.start()
        for job in myqueus:
            job.join()
        for _ in range(n_jobs):
            sums += q.get()
        print("total stocks is {}".format(sums))
        #logging.log(logging.INFO, "Data are saved, total table is {}, save table is {}".format(allcount, sums))



if __name__ == "__main__":
    #names = get_name("allname.txt")
    #stock_code = get_fit_stock(names[:10])
    #print(stock_code)
    my = Job()
    my.savedata_multiprocess()
