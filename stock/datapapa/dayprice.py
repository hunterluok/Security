
import requests
from bs4 import BeautifulSoup
import re
import bs4
import time
import datetime
import multiprocessing

import numpy as np

class DayPrice:
    def __init__(self,
                 ndays=365 * 2):
        self.ndays = ndays

    def singlejob(self):
        pass

    def getHTMLText(self, url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ""

    def getStockStartDate(self, stockCode, ndays):
        html = self.getHTMLText("http://quotes.money.163.com/f10/gszl_" + stockCode + ".html#01f02")
        soup = BeautifulSoup(html, 'html.parser')
        try:
            a = soup.find_all('table', class_="table_bg001 border_box limit_sale table_details")[1]
        except:
            return time.strftime("%Y%m%d")
        cnt = 0
        date = ""
        for tr in a.children:
            if isinstance(tr, bs4.element.Tag):
                tds = tr('td')
                cnt = cnt + 1
                if cnt == 2:
                    date = tds[1].string.replace("-", "")
                    start = str((datetime.datetime.now() - datetime.timedelta(days=ndays)).date()).replace("-", "")
                    if date > start:
                        return ""
                    else:
                        return start
        return date

    def getHistoryTradeInfo(self, stockCode, ndays):
        if stockCode.startswith('0'):
            t_stockCode = '1' + stockCode
        elif stockCode.startswith('6'):
            t_stockCode = '0' + stockCode
        else:
            raise KeyError("WRONG ")

        starts = self.getStockStartDate(stockCode, ndays)
        if starts is None:
            print("this stock is not fit my interest")
            return None
        download_url = "http://quotes.money.163.com/service/chddata.html?code=" + t_stockCode + "&start=" + \
                       starts + "&end=" + time.strftime("%Y%m%d") \
                       + "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"

        print(download_url)
        data = requests.get(download_url)
        data = str(BeautifulSoup(data.text, 'lxml')).split('\r\n')[1:]
        return data


    def save_data(self):
        pass


