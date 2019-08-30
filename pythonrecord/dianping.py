#!/usr/bin/env python
# coding: utf-8

# In[85]:


import requests
from bs4 import BeautifulSoup
import traceback
# 异常处理
import xlwt

import urllib.request


# In[86]:


def get_content(url, headers=None, proxy=None):
    html=requests.get(url, headers=headers).content
    return html

def get_url(html):
    soup =BeautifulSoup(html, 'lxml')
 
    shop_url_list=soup.find_all('div', class_='tit')
    # class是关键字，所以不能直接用，class_就可以了
    # print (shop_url_list)
    # find是只查询一次，find_all()是查询多次返回一个列表，如果没有值就返回空
    # 列表推导式
    return [i.find('a')['href'] for i in shop_url_list]


# In[87]:


def get_detail_content(html):
    try:
        soup=BeautifulSoup(html, 'lxml')
        price=soup.find('span',id='avgPriceTitle').text
        evaluation=soup.find('span',id='comment_score').find_all('span',class_='item')
        # 提取第一个span里面的title属性
        the_star=soup.find('div',class_='brief-info').find('span')['title']
        comments=soup.find('span',id="reviewCount").text
        title=soup.find('div',class_='breadcrumb').find('span').text
        address=soup.find('span',itemprop="street-address")['title']
        # u的意思是代表unicode编码
        print(u'店名:'+title)
        for i in evaluation:
            print(i.text)
        print(price)
        print(u'评价数量:'+comments)
        print(u'地址:'+address.strip())
        print(u'评价星级:'+the_star)
        print('===========================')
        return (title, evaluation[0].text, evaluation[1].text, evaluation[2].text, price, comments, address, the_star)
    except:
        traceback.print_exc()


# In[88]:


items=[]
all_url=[]
 
fk_url=[]
# 将所有商户的评论url全都打印出

for i in range(0, 51):
    start_url='https://www.dianping.com/search/category/344/10/p'+str(i)
    all_url.append(start_url)

base_url='https://www.dianping.com/'


# In[89]:


# 16b49abd26dc8-0a72f636663c7e-133f6e57-13c680-16b49abd26dc8


# In[5]:


# 表头
# 如果不设置cookie有可能导致出现403错误，禁止访问


# In[83]:


headers = ("User-Agent", "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/38.0.2125.122Safari/537.36 SE 2.X MetaSr 1.0")


# In[90]:


# 把多个列表里的url里面的url存储到一个列表里去，便于查询数据
for url in all_url:
    start_html=get_content(url, headers=headers)
    durl= get_url(start_html)
    for i in durl:
        fk_url.append(i)
        print(i)
        
# 列表推导式
# base_url+url打印完整url
url_list=[base_url+url for url in fk_url]
 
for i in url_list:
    detail_html=get_content(i)
    item=get_detail_content(detail_html)
    items.append(item)


# In[20]:


import  urllib.request


# In[18]:


# 
url = 'http://www.dianping.com/shop/103579332'


# In[112]:


"""
headers = ("User-Agent", "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/38.0.2125.122Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = opener.open(url).read()
"""


# #. ip 提取

# In[2]:


import requests


# In[3]:


#请求url，刚才生成的那一串api接口

targetUrl = "http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=959d675c20e1492db1365a388810a5f9&count=10&expiryDate=0&format=2&newLine=2"


# In[37]:


targetUrl = "http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=fc9197f3fbdc493e837f8b54c8e950a8&count=5&expiryDate=0&format=2&newLine=2"


# In[105]:


targetUrl = "http://mvip.piping.mogumiao.com/proxy/api/get_ip_bs?appKey=1df64d23c9a34ad794b7290dd3022363&count=10&expiryDate=0&format=2&newLine=2"

def get_ips(targeturl):
    """
    调用ip池接口
    """
    resp = requests.get(targetUrl)
    
    ips_all = []
    if resp.status_code != 200:
        raise KeyError("status is not 200")
        return 
    else:
        res = resp.text.split('\r\n')
        for ips in res:
            if len(ips) > 1:
                ips_all.append(ips)
                #yield ips
    return ips_all


# In[285]:





# In[99]:


headers = ("User-Agent", "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML,"
                             "like Gecko)Chrome/38.0.2125.122Safari/537.36 SE 2.X MetaSr 1.0")
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# urllib.request.install_opener(opener)
# data = opener.open(url).read()


# In[100]:


def use_proxy(proxy_addr, url):
    """
    使用代理服务器
    """
    try:
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        opener.addheaders = [headers]
        
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    except Exception as e:
        print("exception:" + str(e))
        time.sleep(10)


# In[330]:


ips_all = get_ips(targetUrl)
print(ips_all)

result = {}
for i in ips_all:
    #proxy_addr = "172.20.10.12:1234"
    url = add.format(0)
    proxy_addr = i
    try:
        data = use_proxy(proxy_addr, url) # restaurant_url)
        if data is not None:
            result[i] = data
            print(i)
    except:
        pass


# # 
# 

# In[ ]:


import requests
from lxml import etree
import xlrd
import random
import time

data = []
def Comments(url):
    
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
               'Cookie': '浏览器获取的cookie'
               }
    #url = 'http://www.dianping.com/shop/19110508/review_all?queryType=reviewGrade&queryVal=bad'
    resp = requests.get(url, headers=headers)

    #print (resp.content.decode('utf-8'))#查看爬取网页代码，代码中文内容用二进制表示，故print时要decode

    comments = etree.HTML(resp.text, parser=etree.HTMLParser(encoding='utf-8'))
    commentlong = comments.xpath('//div[@class="review-words Hide"]')#长评
    commentshort = comments.xpath('//div[@class="review-words"]')#短评
    for l in commentlong:
        data.append(l.xpath('string(.)').replace("\t","").replace("\n","").replace(" ","").replace("收起评论","").encode('gbk','ignore').decode('gbk'))
    #把不需要的字符清除，可以用split()去掉\xa0，\t，\n，但是句子会被拆分成一个列表，不方便后续使用
    for s in commentshort:
        data.append(s.xpath('string(.)').replace("\t","").replace("\n","").replace(" ","").encode('gbk','ignore').decode('gbk'))

def getComments():
    path = 'D:/anaconda/shirleylearn/dazhongdianping/negkey.xlsx'#抓取关键字
    excelfile = xlrd.open_workbook(path)
    keys = excelfile.sheet_by_name('Sheet1')
    n = keys.nrows
    for i in range(0,n):
        key = int(keys.row(i)[0].value)
        for page in range(1,int(keys.row(i)[1].value)+1):
            url = 'http://www.dianping.com/shop/%d/review_all/p%d?queryType=reviewGrade&queryVal=bad'%(key,page)#拼链接，修改bad,good即为差评和好评
            #print(url)
            Comments(url)
            time.sleep(random.random())


# In[ ]:





# In[81]:


import re
import urllib.request
import time
import urllib.error


# In[121]:


# ss = 'https://www.ele.me/shop/E3543961203237076510/rate'


# In[322]:


add = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws100sr06gt6&latitude=22.523408&limit=24&longitude=113.937961&offset=0&sign=1560760984692&terminal=web'


# In[144]:


# add = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws100sr06gt6&latitude=22.523408&limit=24&longitude=113.937961&offset={}&restaurant_category_ids%5B%5D=-100&sign=1560760983404&terminal=web'


# In[277]:


import requests
import json
import time
from bs4 import BeautifulSoup
import lxml

# id_list = []#店铺的id列表
# name_list = []#店铺的名称列表
# address_list = []#店铺的地址列表

def get_all_id():
    id_list = []
    name_list = []
    address_list = []
    
    for offset in range(0,985,24):
        # 
        add = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws100sr06gt6&latitude=22.523408&limit=24&longitude=113.937961&offset={}&terminal=web'
        url = add.format(i)
        #url = 'https://www.ele.me/place/ws100sr06gt6?latitude=22.523408&longitude=113.937961'
        #url='https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wx4g06hu38n&latitude=39.91406&limit=24&longitude=116.38477&offset={}&terminal=web'.format(offset)
        web_data = requests.get(url)
        soup=BeautifulSoup(web_data.text, 'lxml')
        content = soup.text
        json_obj = json.loads(content)
        for item in json_obj:
            print(item)
            #item = json.loads(item)
            restaurant_address = item.get('address')
            address_list.append(restaurant_address)
            restaurant_name = item.get('name')
            name_list.append(restaurant_name)
            restaurant_id = item.get('id')
            id_list.append(restaurant_id)
    return name_list,address_list,id_list

name_list,address_list,id_list = get_all_id()


# In[202]:


add = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws100sr06gt6&latitude=22.523408&limit=24&longitude=113.937961&offset={}&terminal=web'
url = add.format(1)
#url = 'https://www.ele.me/place/ws100sr06gt6?latitude=22.523408&longitude=113.937961'
#url='https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wx4g06hu38n&latitude=39.91406&limit=24&longitude=116.38477&offset={}&terminal=web'.format(offset)
#web_data = requests.get(url)
#soup=BeautifulSoup(web_data.text,'lxml')
#content = soup.text
# json_obj = json.loads(content)


# In[254]:


## 
t = result['219.131.214.232:26858']


# In[257]:


ts = json.loads(t)


# In[264]:


ts[0].keys()


# In[267]:


ts[0]['flavors']
ts[0]['delivery_fee_discount']
ts[0].get('float_delivery_fee')
ts[0].get('float_minimum_order_amount')
ts[0].get('float_delivery_fee')


# 
restaurant = item.get('restaurant')
info['地址'] = restaurant.get('address')
info['配送费'] = restaurant.get('float_delivery_fee')
info['名称'] = restaurant.get('name')
info['配送时长'] = restaurant.get('order_lead_time')
info['距离'] = restaurant.get('distance')
info['起送价'] = restaurant.get('float_minimum_order_amount')
info['评分'] = restaurant.get('rating')
info['月销售量'] = restaurant.get('recent_order_num')
info['评分统计'] = restaurant.get('rating_count')
info['风味'] = restaurant.get('flavors')[0].get('name')



import requests
import json
restaurant_url = 'https://www.ele.me/restapi/shopping/v2/menu?restaurant_id=147207648'
web_data = requests.get(restaurant_url)
content = web_data.text
json_obj = json.loads(content)
for item in json_obj:
    for food in item.get('foods'):
        print(food.get('name'))
        print(food.get('tips'))


# In[289]:


json_obj


# In[290]:


import requests
import json

# url = 'https://www.ele.me/restapi/shopping/restaurants?extras[]=activities&geohash=ws101hcw982&latitude=22.52721&limit=30&longitude=113.95232&offset=0&terminal=web'
resp = requests.get(url)
print(resp.status_code)    

Jdata = json.loads(resp.text)
#print Jdata

for n in Jdata:
    name = n['name']
    msales = n['recent_order_num']
    stime = n['order_lead_time']
    tip = n['description']
    phone = n['phone']
    print(name)
