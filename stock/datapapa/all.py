import requests
from bs4 import BeautifulSoup
import re
import bs4
import time
import datetime
import numpy as np
import multiprocessing
import time
import pandas as pd


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockStartDate(stockCode, ndays=365 * 2):
    # 股票上市时间的 选择
    html = getHTMLText("http://quotes.money.163.com/f10/gszl_" + stockCode + ".html#01f02")
    soup = BeautifulSoup(html, 'html.parser')
    try:
        a = soup.find_all('table', class_="table_bg001 border_box limit_sale table_details")[1]
    except:
        return None
        #date = time.strftime("%Y%m%d")
    cnt = 0
    date = ''
    for tr in a.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            cnt = cnt + 1
            if cnt == 2:
                date = tds[1].string.replace("-", "")
                start = str((datetime.datetime.now() - datetime.timedelta(days=ndays)).date()).replace("-", "")
                print("上市 date {} - 数据选取时间 {}".format(date, start))
                if date > start or len(date) != 8:
                    return None
                else:
                    return start
    return None


def getHistoryTradeInfo(stockCode, ndays):
    if stockCode.startswith('0'):
        t_stockCode = '1' + stockCode
    elif stockCode.startswith('6'):
        t_stockCode = '0' + stockCode
    else:
        raise KeyError("WRONG ")

    starts = getStockStartDate(stockCode, ndays)
    if starts is None:
        return None
    # print("start is {}".format(starts))
    download_url = "http://quotes.money.163.com/service/chddata.html?code=" + t_stockCode + "&start=" + starts + "&end=" + time.strftime \
        ("%Y%m%d") + "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    print(download_url)
    data = requests.get(download_url)
    data = str(BeautifulSoup(data.text, 'lxml')).split('\r\n')[1:]
    data = [i.split(',') for i in data]
    return data


def extract(dx):
    price = []
    for line in dx[1:]:
        try:
            price.append([line[0], float(line[3])])
        except:
            print(line)
    return price


def got_lastdata(keys, nday=100):
    l_d = None
    for idx in range(len(keys)):
        print(idx)
        temp_data = getHistoryTradeInfo(keys[idx], ndays=nday)
        if temp_data:
            try:
                ndata = extract(temp_data)
                ndata = pd.DataFrame(ndata, columns=["times", keys[idx]])
                if l_d is None:
                    l_d = ndata
                else:
                    l_d = pd.merge(l_d, ndata, on="times", how="left")
            except:
                pass
    return l_d


def get_name(path):
    datas = []
    with open(path, "r") as f:
        for line in f.readlines():
            datas.append(line.strip())
    return datas


if __name__ == "__main__":
    names = get_name("allname.txt")
    ld = got_lastdata(names[:10])