import sys
from mysql.connector import connection
import pymysql
from mysql.connector.constants import ClientFlag

conn = connection.MySQLConnection(
            host = '127.0.0.1',
            user ='root',
            password = 'root',
            database = 'hs300'
        )
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS hs300_data")

# 创建数据表SQL语句
sql = """CREATE TABLE hs300_data(
         open  float ,
         high float,
         low float,  
         close float )"""

cursor.execute(sql)

# 关闭数据库连接
# conn.close()

sql = "INSERT INTO hs300_data(open, high, low, close) \
VALUES ({}, {}, {}, {})".format(10.1, 20.2, 20, 2000)

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   # 发生错误时回滚
   conn.rollback()


import mysql.connector

cnx = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user ='root',
            password = 'root',
            db = 'lktest',
        )
cur = cnx.cursor()
cur.execute("select * from People limit 50")
for i in cur:
    print(i)
cur.close()
cnx.commit()
cnx.close()

import mysql.connector
from mysql.connector import errorcode
try:
    cnx = mysql.connector.connect(user='root',password='root',
                                database='scrapyDB')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("ok")
    cnx.close()

import mysql.connector
from mysql.connector import errorcode
DB_NAME = 'lktest'
TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='root',passwd='root')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
else:
    print("ok")

