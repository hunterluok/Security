

import numpy as np
import json
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://dc.fanxiaojian.com/order-web/page/main?sid=6&hotelid=1303264&tn=28&t=1576043141199&openid=om9Zq0wVI7RgiYxyJZzWOPG5vGt0"


class PasreData:
    def __init__(self,
                 url,
                 picpath='/Users/luokui/Desktop/xe/',
                 csvpath="../../Desktop/xe/tep.csv"):
        self.name = set(['dishesId', 'dishesName', 'dishesType', 'dishesPrice', 'dishesVipPrice', 'dishesCode', 'dishesImage', 'dishesIntroImage', 'dishesUnit', 'methodCategories'])
        self.url = url
        self.pic_path = picpath
        self.csv_path = csvpath

    def procsee(self):
        p = self.parse(self.url)
        p = p['data']['baseInfo']
        new_data = self.get_data(p)
        self.covert_topd(new_data, self.csv_path)
        wl = self.save_pic(new_data, self.pic_path)
        return wl

    def parse(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        li = []
        for i in soup.find_all("script"):
            li.append(i)
        p = li[1].text.split('\n')[-1].replace("  window._appData = ", "")[0:-1]
        p = json.loads(p)
        if p['code'] != 200:
            raise ConnectionError("网页没法爬取")
        return p

    def get_data(self, p):
        store_infp = p['restaurant']
        food_category = p['foodCategories']
        food_list = p['foodList']
        new_data = []
        for line in food_list:
            temp = {k: v for k, v in line.items() if k in self.name}
            new_data.append(temp)
        return new_data

    def save_pic(self, data, path):
        wrong_list = []
        for line in data:
            name = line['dishesName']
            types = line['dishesType']['dishesTypeName']
            price = line['dishesPrice']
            # vipprice = line['dishesVipPrice']
            url = line['dishesIntroImage']
            pic_path = path + "_".join([name, types, price]) + ".png"
            try:
                pic_content = requests.get(url)
                with open(pic_path, "wb") as f:
                    f.write(pic_content.content)
            except:
                wrong_list.append(line)
        return wrong_list

    def covert_topd(self, new_data, path):
        tep = []
        for line in new_data:
            temp = []
            for key in self.name:
                temp.append(line.get(key, 0))
            tep.append(temp)
        tep = pd.DataFrame(tep, columns=self.name)
        tep.to_csv(path)
        return


if __name__ == "__main__":
    my = PasreData(url)
    my.procsee()
