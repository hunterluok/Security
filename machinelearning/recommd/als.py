

import os
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv("/Users/luokui/laji/ml-100k/u.data", sep="\t", header=None, names=names).head(10000)


spark = SparkSession.builder.master("spark://luokuideMacBook-Pro.local:7077").appName("test.als").getOrCreate()
data = spark.createDataFrame(df)


(trainsss, testing) = data.randomSplit([0.8, 0.2])
(training, valid) = trainsss.randomSplit([0.8, 0.2])

del df


als = ALS(maxIter=10, regParam=0.01, userCol="user_id", itemCol="item_id", ratingCol="rating",
          coldStartStrategy="drop", numBlocks=6)
model = als.fit(training)