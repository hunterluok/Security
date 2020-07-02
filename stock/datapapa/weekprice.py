
import requests
from bs4 import  BeautifulSoup as bs
import json
import csv

#定义两个宏变量。

#宏变量存储目标js的URL列表
STOCKPAGEURL = []
#宏变量存储日期列表，事先爬取
dateList = ['2020-05-22', '2020-05-15',...]
# 生成链接列表的函数。

def Get_Url(num):
    urlFront = 'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&token=4f1862fc3b5e77c150a2b985b12db0fd&cb=jQuery183011315552915535987_1527650090681&id='
    urlRear = '1&type=wk&authorityType=&_=1527650434356'
    for i in range(0, num):
        STOCKPAGEURL.append(urlFront+str(600000+i)+urlRear)

# 获取历史每周价格，关键函数。


def GetInfo(num):
    for i in range(num):
        try:
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
                'Referer': 'http://quote.eastmoney.com/sh603385.html',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'keep-alive',
                'Connection': 'keep-alive'
            }
            pages = requests.get(STOCKPAGEURL[i], headers=headers)
            pages.encoding = 'utf-8'
            texts = pages.text.split('(')[1].split(')')[0]
            stockName = json.loads(texts)
            date = stockName['data'][0].split(',')

            #获取股票的名称、代码和当前价格等基本信息，存储在stockInfo变量中
            stockInfo = []
            stockInfo.append(stockName['name'])
            stockInfo.append(stockName['code'])
            stockInfo.append(stockName['info']['c'])

            #获取股票每周的历史价格，存储在stockInfo变量中
            for i in range(len(dateList)):
                dataListCount = 0
                for j in range(len(stockName['data'])):
                    temp = stockName['data'][j].split(',')
                    if temp[0] == dateList[i]:
                        stockInfo.append(temp[4])
                        break
                    else:
                        dataListCount += 1
                    if dataListCount == len(stockName['data']):
                        stockInfo.append('0')
            #将变量stockInfo的数据存入csv
            CsvDownload(stockInfo)
        except:
            pass


# 将数据存入csv文件中。
def CsvDownload(stockInfo):
    print(stockInfo[1])
    out = open('dataset.csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    csv_write.writerow(stockInfo)


# 主函数，运行上面的函数。
if __name__ == "__main__":
    firstLine = ['name', 'code', 'pricetody'] + dateList
    CsvDownload(firstLine)
    num = 10
    Get_Url(num)
    GetInfo(num)