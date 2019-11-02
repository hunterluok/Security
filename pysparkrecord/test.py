
from __future__ import print_function

import sys
from operator import add
from pyspark.sql import SparkSession

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("ussx <file> ",file=sys.stderr)
        exit(-1)

    spark = SparkSession\
            .builder\
            .appName("test")\
            .getOrCreate()

    lines = spark.read.csv(sys.argv[1]).rdd.map(lambda r:r[0])
    counts = lines.flatMap(lambda x:x.split(' '))\
            .map(lambda x:(x,1))\
            .reduceByKey(add)

    output = counts.collect()
    for (word, count) in output:
        print("{0}:{1}".format(word, count))
    spark.stop()
