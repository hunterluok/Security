#encoding:utf-8
from pyspark.sql import SparkSession
import sys
from  random import  random
from operator import add
import time

if __name__ =="__main__":
    start = time.time()
    spark = SparkSession.builder.appName("xx").getOrCreate()

    def f(_):
        x = random() * 2 -1
        y = random() * 2 -1
        return 1 if x**2 + y**2 <=1 else 0


    if len(sys.argv)>2:
        print("the parameter is wrong")
    elif len(sys.argv)==1:
        partitions = 2
        n = 10000 * partitions
    elif len(sys.argv)==2:
        print("num of 1 args {}".format(sys.argv[0]))
        partitions = int(sys.argv[1])
        print("partitions is {}".format(partitions))
        n = 10000 * partitions
    else:
        print("wrong")
       # break
    # n = 1000000 * partitions
    cout = spark.sparkContext.parallelize(range(1,n+1),partitions).map(f).reduce(add)

    print("pi ={}...".format(4.0 * cout/n))
    print(partitions)
    print(" 用时 。。。{}".format(time.time()-start))
    spark.stop()



                
