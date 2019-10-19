
# coding: utf-8



import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("appName").master("local[*]").getOrCreate()
#from pyspark.sql import Row
from pyspark.sql import HiveContext
sqlc = HiveContext(spark)


data = sqlc.createDataFrame([(1,"a"),(3,"b")],['a','b'])
t = np.array(data.toPandas())
m,_ = t.shape



#_*_ coding:utf-8 _*_
import phoenixdb
import phoenixdb.cursor
import datetime
import time
import numpy as np
import os

database_url = 'http://10.81.33.156:8765'
conn = phoenixdb.connect(database_url, autocommit=True)
cursor=conn.cursor()


cursor.execute("SELECT * FROM dztz_data_616  limit 1000")
data = cursor.fetchall()

sql="UPSERT INTO faka_data_616 values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
for i in range(N):
    cursor.execute(sql.format(i,str(data[i][0]),str(data[i][1]),str(data[i][2]),str(data[i][3]),str(data[i][4]),str(data[i][5]),str(data[i][6]),str(data[i][7]),str(data[i][8]),str(data[i][9]),str(data[i][10]),str(data[i][11]),str(data[i][12]),str(data[i][13]),str(data[i][14]),str(data[i][15]),str(data[i][16]),str(data[i][17]),str(data[i][18]),str(data[i][19]),str(data[i][20]),str(data[i][21]),str(data[i][22]),str(data[i][23]),str(data[i][24]),str(data[i][25]),str(data[i][26]),str(data[i][27]),str(data[i][28]),str(data[i][29]),str(data[i][30]),str(data[i][31]),str(data[i][32]),str(data[i][33]),str(data[i][34]),str(data[i][35]),str(data[i][36]),str(data[i][37]),str(data[i][38]),str(data[i][39]),str(data[i][40]),str(data[i][41]),str(data[i][42]),str(data[i][43]),str(data[i][44]),str(data[i][45])))


sql="UPSERT INTO faka_data_616 values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
for i in range(N):
    cursor.execute(sql.format(i,data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7],data[i][8],data[i][9],data[i][10],data[i][11],data[i][12],data[i][13],data[i][14],data[i][15],data[i][16],data[i][17],data[i][18],data[i][19],data[i][20],data[i][21],data[i][22],data[i][23],data[i][24],data[i][25],data[i][26],data[i][27],data[i][28],data[i][29],data[i][30],data[i][31],data[i][32],data[i][33],data[i][34],data[i][35],data[i][36],data[i][37],data[i][38],data[i][39],data[i][40],data[i][41],data[i][42],data[i][43],str(data[i][44]),str(data[i][45]))


data.encode('utf-8')
cursor.execute("select * from TEST789 limit 2")
t =cursor.fetchall()

