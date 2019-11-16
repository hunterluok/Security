import torch
import cv2
import os
import multiprocessing
import time
import numpy as np
import cProfile
import pstats


class ReadPicture:
    def __init__(self,
                 path="/home/fordl/pytorch/faces/",
                 n_jobs=-1):

        self.im_path = path
        if n_jobs == -1:
            self.n_jobs = multiprocessing.cpu_count()
            print("n_jobs is {}".format(self.n_jobs))
        elif isinstance(n_jobs, int) and n_jobs > 0:
            self.n_jobs = n_jobs
        else:
            raise ValueError("n_jobs must be int and greater than 0")

    def single_thread(self):
        last = []
        lists = os.listdir(self.im_path)
        lists = [self.im_path + i for i in lists if i.endswith('.jpg')]
        for line in lists:
            temp = cv2.imread(line, 1)
            last.append(temp)
        return last

    def myjob(self, q, list_data):
        new = []
        for pic in list_data:
            temp_data = cv2.imread(pic, 1)
            name = pic.split("/")[-1]
            new.append(name)
            # print(temp_data.shape, "-- data shape", name)
            # new.append(temp_data)
        q.put(new)

    def split(self):
        lists = os.listdir(self.im_path)
        lists = [self.im_path + i for i in lists if i.endswith('.jpg')]
        lens = len(lists)
        if lens < 1:
            return ValueError
        print(" picture total is {}".format(lens))
        print(" a sample is {}".format(lists[0]))
        print(" data shape is {}".format(cv2.imread(lists[0]).shape))
        batch = (lens - 1) // self.n_jobs + 1
        for i in range(self.n_jobs):
            yield lists[i * batch: (i + 1) * batch]

    def multi_read(self):
        job_queue = []
        q = multiprocessing.Queue()
        data = []

        for index, sub_data in enumerate(self.split()):
            temp_job = multiprocessing.Process(target=self.myjob,
                                               args=(q, sub_data), name="process_{}".format(index))
            job_queue.append(temp_job)

        for jobs in job_queue:
            jobs.start()
        for jobs in job_queue:
            jobs.join()
        for _ in range(self.n_jobs):
            data.extend(q.get())
        return data


if __name__ == "__main__":
    start = time.time()
    my = ReadPicture(n_jobs=4)
    # data = my.multi_read()
    data = my.single_thread()
    cProfile.run("my.single_thread()", "prof.txt")
    p = pstats.Stats("prof.txt")
    p.sort_stats("time").print_stats()
    # print(np.array(data).shape)
    # dx = data[0]
    # cv2.imshow("dx", dx)
    # cv2.waitKey(0)
    print("used time is {}".format(time.time() - start))
