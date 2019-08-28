
import os
from hdfs.client import Client

import requests
import redis
import re
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


client = Client("http://192.168.31.51:50070")

def all_files_path(first_path='/dazhongdianping/sz/'):
    """将hdfs中存储的页面源码加入到待解析的队列中
    :param path:hdfs文件路径
    :return: hdfs文件list
    """
    file_list = []
    for root, dirs, files in client.walk(first_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            all_files_path(dir_path)
    return file_list

res = all_files_path()


ip_list = []
session = requests.session()
headers = {'User-Agent': UserAgent().random}
page = session.get("http://www.xicidaili.com/nn", headers=headers)


soup = BeautifulSoup(page.text, 'lxml')
taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
