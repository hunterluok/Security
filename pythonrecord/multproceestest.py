###
import threading
import time
import _thread
from queue import Queue
import numpy as np
from multiprocessing import Pool

# 新线程执行的代码:

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def print_hello():
    n = 0
    while n < 5:
        n += 1
        time.sleep(1)
        print("hello world", time.ctime(time.time()))



print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t1 = threading.Thread(target=print_hello, name="hel")
t.start()
t1.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)



# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


def print_times(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        temp = 'hello threading'
        print("%s, %s: %s" % (temp, threadName, time.ctime(time.time())))


# 创建两个线程
start = time.time()
try:
    _thread.start_new_thread(print_time, ("Thread-1", 1,))
    _thread.start_new_thread(print_times, ("Thread-2", 1,))
except:
    print("Error: unable to start thread")
print(time.time() - start)


class myThread(threading.Thread):
    def __init__(self, threadid, name, counter):
        threading.Thread.__init__(self)
        self.threadid = threadid
        self.name = name
        self.counter = counter

    def run(self):
        print("starting " + self.name)
        # 获取锁之后才能运行。
        # threadLock.acquire()
        # threading.Lock().acquire()
        print_time(self.name, self.counter, 3)
        # threadLock.release()
        # threading.Lock().release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
# for t in threads:
#  t.join()
print("Exiting Main Thread")


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)


data = [[1,2,3], [4,5,6], [7, 8,9]]
#data = np.arange(1000000).reshape(100000, 10)
def multi(data):
    lens = len(data)
    q = Queue()
    threads = []
    for i in range(lens):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thre in threads:
        thre.join()
    print(threading.active_count())
    results = []
    for _ in range(lens):
        results.append(q.get())
    #for thre in threads:
        #thre.clear()
    print(results)



start = time.time()
multi(data)
time.time() - start


def cal(data):
    temp = []
    for line in data:
        for j in range(len(line)):
            line[j] = np.power(j, 2)
        temp.append(line)
    return temp


start = time.time()
s = cal(data)
time.time() - start



def f(x):
    return x* x

p = Pool(5)
p.map(f, [1, 2, 3])


import subprocess
import multiprocessing


r = subprocess.call(['nslookup', 'www.python.org'])
multiprocessing.cpu_count()