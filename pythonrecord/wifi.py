#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:


import os
import time
 
class App():
 
    def __init__(self,count):
        self.count = count
 
    # 开启wifi的方法
    def openWifi(self):
        cmd = 'adb shell svc wifi enable'
        os.popen(cmd)
        time.sleep(60)
 
    # 关闭wifi的方法
    def closeWifi(self):
        cmd = 'adb shell svc wifi disable'
        time.sleep(5)
 
    #控制wifi循环的方法
    def controlWifi(self):
        i = 1
        while (self.count >0):
            print("第 %d 次执行开关Wi-Fi操作" % i)
            self.closeWifi()
            self.openWifi()
            i = i +1
            self.count = self.count - 1


# In[ ]:


#控制Wi-Fi开关执行100次
app = App(100)
app.controlWifi()


# In[ ]:





# In[ ]:


import time
import subprocess
i = 0
#每次操作的间隔时间取决于手机配置，配置越高时间越短
sleep_time = 0.5 
while 1:
        #用popen设置shell=True不会弹出cmd框
        process = subprocess.Popen('adb shell input tap 14 1402', shell=True)
        time.sleep(sleep_time)
        process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
        time.sleep(sleep_time)
        process = subprocess.Popen('adb shell input tap 375 1402', shell=True)
        time.sleep(sleep_time)
        process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
        time.sleep(sleep_time)
       #os.system('adb shell input tap 14 1402')
        #os.system('adb shell input keyevent KEYCODE_BACK')
        #os.system('adb shell input tap 375 1402')
        i+=1
        print  str(i) + 'clicks have been completed'


# In[ ]:





# In[2]:


from bs4 import BeautifulSoup
import requests
import sys
import json


# In[3]:


#cfgcookie.txt人工输入的cookie
def getcookiestr(path):
    '''
    path:配置文件路径
    '''
    try:
        dicookie = {}
        with open(path + r'cfgcookie.txt', 'r') as r:
            inputstr = r.read()
            for one in inputstr.split('; '):
                dicookie[one.split('=')[0]] = one.split('=')[1]
        #    for x,y in dicookie.items():
        #        print (type(y))
        print(dicookie)
        return dicookie
    except Exception as e:
        print (str(e))
        print (u'请检查cfgcookie.txt配置文件正确性！')


# In[ ]:


#cfgcookie.txt人工输入的cookie    
#newcookie.json记录每次操作后更新的cookie
def getcookies(path):
    '''
    path:配置文件路径
    '''
    try:
        dicookie = {}
        with open(path + r'newcookie.json','r') as r:
            try:
                dicookie = json.load(r)
                print (dicookie)
            except Exception as e:
                print (str(e))
                #newcookie.json读取错误之后读取cfgcookie.txt
                with open(path + r'cfgcookie.txt', 'r') as r:
                    inputstr = r.read()
                    for one in inputstr.split('; '):
                        dicookie[one.split('=')[0]] = one.split('=')[1]
                #    for x,y in dicookie.items():
                #        print (type(y))
        return dicookie
    except Exception as e:
        print (str(e))
        print (u'请检查cfgcookie.txt配置文件正确性！')


# In[4]:


def savenewcookie(path, dicookie):
    '''
    存储最新的cookie
    path:配置文件路径
    dicookie:存储的dict
    '''
    try:
        with open(path + r'newcookie.json','w') as w:
            json.dump(dicookie,w)
    except Exception as e:
        print (str(e))
        print (u'存储newcookie.json出错了！')


# In[5]:


def get_dianping(scenic_url):
    proxies = {
#    "http": "50.233.137.33:80",
    "http":"218.59.139.238:80",
    }
    headers = {
        'Host': 'www.dianping.com',
        'Referer': 'http://www.dianping.com/shop/22711693',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/535.19',
        'Accept-Encoding': 'gzip'
    }
    headers['Referer'] = scenic_url.replace('https', 'http').replace('/review_all', '')
#    cookies = {'cy':'835', 
#                   'cye':'guanyun', 
#                   '_lxsdk_cuid':'16426247fafc8-0cf040f6fc4a118-4c312b7b-100200-16426247fafc8',
#                   '_lxsdk':'16426247fafc8-0cf040f6fc4a118-4c312b7b-100200-16426247fafc8',
#                   '_hc.v':'7b5b3de6-776c-46d2-e7d3-e468d13446dc.1529648284',
#                   '_dp.ac.v':'c584c92c-95aa-4220-a4e0-bb40878ae863',
#                   'ua':'15366181451',
#                   's_ViewType':'10', 
#                   '_lxsdk_s':'1644ec042ce-f7f-0ee-489%7C%7C1176',
#                   'cityInfo':'%7B%22cityId%22%3A835%2C%22cityEnName%22%3A%22guanyun%22%2C%22cityName%22%3A%22%E7%81%8C%E4%BA%91%E5%8E%BF%22%7D',
#                   '__mta':'146585483.1530329665619.1530330562343.1530330863738.6',
#                   'ctu':'4a3974cdf5b2e5b0fd3b2d9a6ec23a7d48c74ae4f2a36e72bfed34b59b322f331e42d186b52cd0db5fa5a045e40f22d4',
#                   'dper':'79ff66a7e0fc79b70c8ac58013ca79eda9a3b87d62b5ad42a670e8244ddcbba0ee1a751db6a8e0ff39608623d5575eb1e6f8237e50713a9455f35c1d81ef75cbed81c68fc95315a4c2dde5930e0a840d14eddc61aee31c213f59c602aba3d13d',
#                   'll':'7fd06e815b796be3df069dec7836c3df',
#                   '_lx_utm':'utm_source%3DBaidu%26utm_medium%3Dorgani'}
    # 之前的cookie已过期
    cookies = {'cy':'835', 
                   'cye':'guanyun', 
                   '_lxsdk_cuid':'165326abb16c8-0b4257bdbfb683-4c312b7b-144000-165326abb17c8',
                   '_lxsdk':'165326abb16c8-0b4257bdbfb683-4c312b7b-144000-165326abb17c8',
                   '_hc.v':'f342b8f4-76bd-b7e3-f311-dde38460f6a9.1534149181',
                   'ua':'15366181451',
                   '_lxsdk_s':'16532c04c62-0a1-332-21f||51',
                   'ctu':'984140a059b7ea17dc9cf8a1beabdc7a327e77fb491f3f781040b77efe2e8459',
                   'dper':'79ff66a7e0fc79b70c8ac58013ca79ed63f150e8da4061cd8c570a3e17266cfad5d17e745b95f2276ca66f1c978ffe8e7c12c3e228110081542c4a8ebd9518951784feb7aa8b609eec66fc66f67c483cb7fb7f1c56f991490523848b82b003ec',
                   'll':'7fd06e815b796be3df069dec7836c3df'}

#    cookies= getcookiestr('.\\')

#    cookies = {,
#        '_lxsdk_cuid': '16146a366a7c8-08cd0a57dad51b-32637402-fa000-16146a366a7c8',
#        '_lxsdk': '16146a366a7c8-08cd0a57dad51b-32637402-fa000-16146a366a7c8',
#        '_hc.v': 'ec20d90c-0104-0677-bf24-391bdf00e2d4.1517308569',
#        's_ViewType': '10',
#        'cy': '16',
#        'cye': 'wuhan',
#        '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
#        '_lxsdk_s': '1614abc132e-f84-b9c-2bc%7C%7C34'
#    }
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False

    returnList = []
#    url = "https://www.dianping.com/shop/%s/review_all" % scenic_id
    r = requests.get(scenic_url, headers=headers, cookies=cookies, proxies = proxies)#
#    print r.text

    with open(r'downloade0.html','wb') as w:
            w.write(r.text.encode('utf-8'))
    soup = BeautifulSoup(r.text, 'lxml')
#    print soup
    lenth = soup.find_all(class_='PageLink').__len__() + 1
    print ("lenth:%d"%(lenth))

    title = soup.select_one('.shop-name')
    try:
        title = title.get_text()
    except Exception as e:
        pass
    print ("title:%s"%(title))
    coment = soup.select('.reviews-items ul li')

    for one in coment:
        try:
            if one['class'][0]=='item':
                continue
        except Exception:
            pass
        time = one.select_one('.main-review .time')
        time = time.get_text().strip()
        print ("time:%s"%(time))
        name = one.select_one('.main-review .dper-info .name')
        name = name.get_text().strip()
        print ("name:%s"%(name))
        star = one.select_one('.main-review .review-rank span')
        star = star['class'][1][7:8]
        print ("star:%s"%(star))
        pl = one.select_one('.main-review .review-words')
        words = pl.get_text().strip().replace(u'展开评论','')
        print ("word:%s"%(words))
        returnList.append([title,time,name,words,star])
        print ('=============================================================')
    if lenth > 1:
        headers['Referer'] = scenic_url.replace('https', 'http')
        for i in range(2,lenth+1):
            urlin = scenic_url + '/p' + str(i)
            r = requests.get(urlin, headers=headers, cookies=cookies, proxies = proxies)
            with open(r'downloade.html','wb') as w:
                w.write(r.text.encode('utf-8'))
#            print r.text
            soup = BeautifulSoup(r.text, 'lxml')
            title = soup.select_one('.shop-name')
            title = title.get_text()
            print ("title:%s"%(title))
            coment = soup.select('.reviews-items ul li')

            for one in coment:
                try:
                    if one['class'][0]=='item':
                        continue
                except Exception:
                    pass
                time = one.select_one('.main-review .time')
                time = time.get_text().strip()
                print ("time:%s"%(time))
                name = one.select_one('.main-review .dper-info .name')
                name = name.get_text().strip()
                print ("name:%s"%(name))
                star = one.select_one('.main-review .review-rank span')
                star = star['class'][1][7:8]
                print ("star:%s"%(star))
                pl = one.select_one('.main-review .review-words')
                words = pl.get_text().strip().replace(u'展开评论','').replace(u'收起评论','')
                print ("word:%s"%(words))
                returnList.append([title,time,name,words,star])
                print ('=============================================================')
    return returnList


# In[6]:


def atest():
    headers = {
        'Host': 'www.baidu.com',
        'Referer': 'https://www.baidu.com/link?url…6885dc00070b51000000035b3765f4',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/535.19',
        'Accept-Encoding': 'gzip'
    }
    cookies= getcookiestr('.\\')
    cookies = requests.utils.cookiejar_from_dict(cookies, cookiejar=None, overwrite=True)
    resion = requests.Session()
    resion.cookies = cookies
    r = resion.get('https://www.baidu.com/', headers=headers)
    savenewcookie('.\\', r.cookies.get_dict())#存储更新后的cookie


# In[14]:


#if __name__ == "__main__":
# http://www.dianping.com/shop/125403584
# get_dianping('http:/www.dianping.com/shop/125403584/review_all')
#    
# atest()


# In[ ]:


requests.get('http://www.dianping.com/shop/125403584')


# In[ ]:





# In[8]:


# 
import requests


# In[8]:


resu = requests.get(url='http://www.dianping.com/shop/125403584')


# In[ ]:





# In[ ]:


####### 


# In[1]:


import requests
from bs4 import BeautifulSoup
import traceback
# 异常处理
import xlwt
# 写入xls表
# Cookie记录登录信息，session请求


# In[ ]:


def get_content(url,headers=None,proxy=None):
 
    html=requests.get(url,headers=headers).content
    return  html
 

def get_url(html):
    soup =BeautifulSoup(html,'lxml')
 
    shop_url_list=soup.find_all('div',class_='tit')
    # class是关键字，所以不能直接用，class_就可以了
    # print (shop_url_list)
    # find是只查询一次，find_all()是查询多次返回一个列表，如果没有值就返回空
    # 列表推导式
    return [i.find('a')['href'] for i in shop_url_list]


def get_detail_content(html):
    try:
        soup=BeautifulSoup(html,'lxml')
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


# In[ ]:



if __name__ =='__main__':

   items=[]
   all_url=[]

   fk_url=[]
   # 将所有商户的评论url全都打印出
   for i in range(0,51):
       start_url='https://www.dianping.com/search/category/344/10/p'+str(i)
       all_url.append(start_url)

   base_url='https://www.dianping.com/'
   # 表头
   # 如果不设置cookie有可能导致出现403错误，禁止访问
   headers={
       'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebkit'
        'Cookie' '_lxsdk_cuid = 15c862ce29774 - 0e90b90a55f72 - 414a0229 - 1fa400 - 15c862ce299c8;_lxsdk = 15c862ce29774 - 0e90b90a55f72 - 414a0229 - 1fa400 - 15c862ce299c8;_hc.v = 77b1169f - 1763 - c5b6 - ade2 - a81093a8b4cd.1496899708;PHOENIX_ID = 0a010725 - 15c862cf0e2 - 207bfe7;JSESSIONID = 6AEA99FE3A5B0BF2920C833821F8D711;aburl = 1;cy = 344;cye = changsha;_lxsdk_s = 15c862ce29c - ce2 - f25 - 8c % 7C % 7C84;__mta = 219083046.1496899711367.1496902358445.1496902376486.8'
   }
   # 把多个列表里的url里面的url存储到一个列表里去，便于查询数据
   for url in all_url:
       start_html=get_content(url)
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

   newTable='DZDPdemo1.xls'
   wb=xlwt.Workbook(encoding='utf-8')
   ws=wb.add_sheet('test1')
   headData=['商户名字','口味评分','环境评分','服务评分','人均价格','评论数量','地址','商户星级']
   for column in range(0,8):
       # 0把行定位到第一行了列 后面是设置字体
       ws.write(0,column,headData[column],xlwt.easyxf('font:bold on'))


   index =1

   lens=len(items)
   print(u'数据总长度='+str(lens))
   # 有多少数据
   # 只对列做了一个for循环，因为行列都要写入，所以做两个for循环
   # 多少行由列表数据决定的，有多少数据就有多少行
   # index代表的是行，我们从1开始是因为标题已经占据了第一行
   # 对list做了两次索引，第一次是商户信息拿出来，第二个索引是把商户的详细信息拿出来
   # 简单的来说，j就代表一个商户，i[0]相当于代表店名，i[1]相当于代表evaluation[0].text依次类推
   for j in range(0,lens):
       for i in range(0,8):
           ws.write(index ,i,items[j][i])
       index+=1
   wb.save(newTable)


# In[ ]:





# In[ ]:


### 


# In[ ]:




