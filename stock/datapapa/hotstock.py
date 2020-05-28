
import multiprocessing

import requests
from bs4 import BeautifulSoup
import re
import bs4
import time

import numpy as np


class Job:
    def __init__(self,
                 n_page=100,
                 n_jobs=4,
                 name_path="name.txt",
                 hot_path="hot.txt"):
        self.n_page = n_page
        self.n_jobs = n_jobs
        self.name_path = name_path
        self.hot_path = hot_path

    def split_data(self, n_jobs):
        page_list = np.arange(1, self.n_page + 1)
        indexs = int((self.n_page - 1) / n_jobs) + 1
        for id in range(n_jobs):
            yield page_list[indexs * id: (id + 1) * indexs]

    def savedata_multiprocess(self):
        # logging.log(logging.INFO, "db infomation are {}".format(mins))
        if self.n_jobs == -1:
            # 获取 cpu的个数
            n_jobs = multiprocessing.cpu_count() - 2
        else:
            n_jobs = self.n_jobs

        q = multiprocessing.Queue()
        myqueus = []
        sums = 0
        for ids, p_list in enumerate(self.split_data(n_jobs)):
            temp_job = multiprocessing.Process(target=self.get_latest, args=(q, p_list), name="jon_{}".format(ids))
            myqueus.append(temp_job)
        for job in myqueus:
            job.start()
        for job in myqueus:
            job.join()
        for _ in range(n_jobs):
            sums += q.get()
        print("total stocks is {}".format(sums))
        #logging.log(logging.INFO, "Data are saved, total table is {}, save table is {}".format(allcount, sums))

    def get_latest(self, q, page_list):
        # 获取若干页的数据
        myhot = {}
        mymaps = {}
        for i in page_list:
            d = requests.get("http://guba.eastmoney.com/default,0_{}.html".format(i))
            soup = BeautifulSoup(d.text, 'lxml')
            res = soup.find_all(class_="balink")
            maps, hot = self.get_gubai(res)
            mymaps.update(maps)
            for key in hot.keys():
                if key in myhot.keys():
                    myhot[key] += hot[key]
                else:
                    myhot.setdefault(key, hot[key])
        counts = len(myhot.keys())
        if self.name_path:
            self.save_data(self.name_path, mymaps)
            print("saved name")
        if self.hot_path:
            self.save_data(self.hot_path, myhot)
            print("saved hot")
        q.put(counts)

    def save_data(self, path, dict_data):
        with open(path, "a") as f:
            for key, value in dict_data.items():
                line = " ".join([key, str(value)])
                f.write(line + '\n')

    def get_gubai(self, res, save=('0', '6')):
        # '603321': ['梅轮电梯吧', '/list,603321.html']
        maps = {}
        hot = {}
        for line in res:
            temp_line = line['href']
            ids = temp_line.split(',')[1].split('.')[0]
            if ids[0] not in save:
                    continue
            name = line.string
            maps.setdefault(ids, [name, temp_line])
            hot.setdefault(ids, 0)
            hot[ids] += 1
        return maps, hot


if __name__ == "__main__":
    myobj = Job(n_page=10, n_jobs=2)
    myobj.savedata_multiprocess()