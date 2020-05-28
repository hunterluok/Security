
import requests
from bs4 import BeautifulSoup
import re


def getHTMLpages(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 将股票信息存入列表
def getSharelist(html):
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all('a', target="_blank") # a标签的target属性值为"_blank"
    sets = set()
    for tag in tags:
        str1 = tag.attrs['href']  # 获得链接信息
        match = re.search(r's[hz]\d{6}', str1)  # 从链接中找到股票代码
        if match:  # 必须加判断，因为有的链接不符合，这样的话正则表达式匹配不到，match.group(0)就是空的，会报错TypeError
            name = match.group(0)
            if name[2] in ('0', '6'):
                sets.add(name[2:])
        else:
            continue
    return sets


if __name__ == "__main__":
    url1 = "http://quote.eastmoney.com/stock_list.html"
    html = getHTMLpages(url1)

    mystock = getSharelist(html)
    print(mystock)


