

import pymongo
import pandas as pd

import logging
import multiprocessing
import time


log_format = "%(asctime)s - %(levelname)s - %(message)s"
date_format = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.INFO, filename='my.log', filemode='w', format=log_format, datefmt=date_format)


class ProcessDataSingleThread:
    def __init__(self, ips, ports):
        paths = "mongodb://{}:{}/".format(ips, ports)
        self.client = pymongo.MongoClient(paths)

    def get_dbinfor(self):
        client = self.client
        if client is not None:
            allcount = 0
            names = client.list_database_names()
            logging.log(logging.INFO, "db names are {}".format(names))
            mins = {}
            for name in names:
                db = client[name]
                mins.setdefault(name, {})
                col_name = db.list_collection_names()
                for col in col_name:
                    mins[name][col] = db[col].find().count()
                    allcount += 1
            return mins, allcount
        else:
            logging.log(logging.ERROR, "mongodb is not connected")
            return None

    def trans_table(self, target_table):
        cols = []
        for key in target_table.find_one({}, {"_id": 0, "id": 0}):
            cols.append(key)
        data = []
        for line in target_table.find({}, {"_id": 0, "id": 0}):
            temp = []
            for value in line.values():
                temp.append(value)
            data.append(temp)
        data = pd.DataFrame(data, columns=cols)
        return data


class ProcessData(ProcessDataSingleThread):
    def __init__(self, ips, ports, n_jobs=-1):
        super(ProcessData, self).__init__()
        self.paths = "mongodb://{}:{}/".format(ips, ports)
        self.n_jobs = n_jobs

    def split_data(self, dict_datas, n_jobs):
        lens = len(dict_datas)
        db_nameslist = [key for key in dict_datas.keys()]
        indexs = int((lens - 1) / n_jobs) + 1
        for id in range(n_jobs):
            yield db_nameslist[indexs * id: (id + 1) * indexs]

    def savedata_multiprocess(self):
        mins, allcount = self.get_dbinfor()
        logging.log(logging.INFO, "db infomation are {}".format(mins))

        if self.n_jobs == -1:
            # 获取 cpu的个数
            n_jobs = multiprocessing.cpu_count()
        else:
            n_jobs = self.n_jobs

        def myjob(q, dbname, db_infor):
            counts = self.savedata_tocsv(dbname, db_infor)
            q.put(counts)

        q = multiprocessing.Queue()
        myqueus = []
        sums = 0
        for ids, mydbname in enumerate(self.split_data(mins, n_jobs)):
            temp_job = multiprocessing.Process(target=myjob, args=(q, mydbname, mins), name="jon_{}".format(ids))
            myqueus.append(temp_job)
        for job in myqueus:
            job.start()
        for job in myqueus:
            job.join()
        for _ in range(n_jobs):
            sums += q.get()
        logging.log(logging.INFO, "Data are saved, total table is {}, save table is {}".format(allcount, sums))

    def savedata_tocsv(self, dbnames, mins):
        # fork（）的原因，每次会启动一个线程。因为 父子线程不共享一个
        # Care must be taken when  using  instances  of  MongoClient
        # with fork().Specifically, instances of MongoClient must not be copied
        # from a parent process to a child process.Instead,
        #  the parent process and each child process must create
        #  their own instances of MongoClient.
        client = pymongo.MongoClient(self.paths)
        count = 0
        if client is None:
            logging.log(logging.ERROR, "client is not start, count is {}".format(count))
            return count
        for db_name in dbnames:
            db = client[db_name]
            for table_name in mins[db_name].keys():
                tables = db[table_name]
                save_table_name = "{}_{}".format(db_name, table_name)
                try:
                    data = self.trans_table(tables)
                    data.to_csv("{}.csv".format(save_table_name))
                    logging.log(logging.INFO, "Save the data {}".format(save_table_name))
                    count += 1
                except:
                    with open("wronginfo", "a+") as f:
                        f.write("Wrong!! save {} is wrong".format(save_table_name) + '\n')
                    logging.log(logging.WARN, "Wrong!! save {} is wrong".format(save_table_name))
        return count


if __name__ == "__main__":
    my = ProcessData(n_jobs=-1, ips="0.0.0.0", ports="6666")
    start = time.time()
    my.savedata_multiprocess()
    print("multi use time {}".format(time.time() - start))

