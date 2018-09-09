
# coding: utf-8

# In[1]:


import numpy as np
from numpy import *


# In[2]:


def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

#frozenset([1,2])
data = loadDataSet()


# In[4]:


"""
def createC1(dataSet):
    C1 = set()
    for transaction in dataSet:
        for item in transaction:
            if not item in C1:
                C1 = C1 | set([item])
    #C1.sort()
    return frozenset(C1)
createC1(data)
"""


# In[119]:


bag_fisrt = first_create(data)
bag_fisrt


# In[121]:


freq_item,item_set = cal_support(data,minsupport=0.5,bags=bag_fisrt)
freq_item,item_set


# In[124]:


bag1 = create_set(item_set,2)
bag1


# In[125]:


freq_item_1,item_set_1 = cal_support(data,minsupport=0.5,bags=bag1)
freq_item_1,item_set_1


# In[126]:


bag2 = create_set(item_set_1,k=3)
bag2


# In[127]:


freq_item_2,item_set_2 = cal_support(data,minsupport=0.5,bags=bag2)
freq_item_2,item_set_2


# In[9]:


# 创建初始化bag
def first_create(data):
    bag ={}
    for i in data:
        for j in i:
            bag.setdefault(tuple([j]),0)
            bag[tuple([j])]+=1
    return bag

# 构建 bag 后续使用
def createC2(dataSet,bag):
    C1 = {}
    for transaction in dataSet:
        for i in bag:
            if set(i).issubset(set(transaction)):
                C1.setdefault(i,0)
                C1[i] +=1
    C1 = sorted(C1.items(),key=lambda row:row[1],reverse=True)
    return C1

# 构建 高频词组 过滤低频词组。 
def cal_support(data,minsupport,bags):
    dic_c1 = createC2(data,bags)
    m = len(data)
    dic_n = {k:v/m for k,v in dic_c1}
    dic_new = {k:v for k,v in dic_n.items() if v>=minsupport}
    item_set = [k for k in dic_new.keys()]
    return dic_new,item_set

# 构建新的 候选集合。
from itertools import combinations as cchose
def create_set(item_set,k):
    if k>len(item_set):
        raise KeyError("The value is wrong")
    if isinstance(item_set,list):
        pass
    else:
        raise KeyError("Wrong")
        
    z =set()
    for i in item_set:
        for j in i:
            z |=set([j])
    z = list(z)
    
    temp = list(cchose(z,k))
    item_set = np.array(item_set)
    
    new_items = []
    for i in temp:
        temp_tuple=()
        for j in i:
            temp_tuple +=tuple([j])
        new_items.append(temp_tuple)
    return new_items

def find_max_freq(data,minsup=0.5):
    freq_items = []
    item_sets = []
    
    # item_set is a list of candidate itemsets
    bag_first = first_create(data)
    freq_item,item_set = cal_support(data,minsupport=0.5,bags=bag_first)
    
    freq_items.append(freq_item)
    item_sets.append(item_set)
    
    i = 2
    while i>1:
        
        bag1 = create_set(item_set,k=i)
        freq_item,item_set = cal_support(data,minsupport=minsup,bags=bag1)
        
        freq_items.append(freq_item)
        item_sets.append(item_set)
        i += 1
        
        if len(item_set)<=i:
            break
    return freq_items,item_sets
            
a,b=find_max_freq(data,minsup=0.5)

def get_rule(data,minsup=0.5,minconf=0.5):
    candi,_ = find_max_freq(data,minsup=minsup)
    length = len(candi)
    rules = []
    
    count=1
    for j in range(-length+1,0):
        for a,b in candi[j].items():              # Supper itemset 
            for i in range(-length,j,1):          # 注意这个地方需要注意。
                for x,y in candi[i].items():      # sub itemset
                    if set(x).issubset(set(a)) and b / y > minconf:
                        temp = set(a)-set(x)
                        rule = ["rule{}: qx{} ===> re{}. freq_set({}),conf:{:.2f},Qsup_{:.2f},Rsup_{:.2f}"                                .format(count,x,temp,a,b/y,y,b)]
                        rules.append(rule)
                        count += 1
    return rules


# In[118]:


get_rule(data,minconf=0.7)


# In[119]:


path ='/Users/luokui/Documents/机器学习实战/机器学习实战及配套代码/machinelearninginaction/Ch11/mushroom.dat'

def get_data(path):
    with open(path,'r') as f:
        data = []
        line = f.readline()
        while line:
            #line =[float(i) for i in line.strip().split()]
            line = line.strip().split()
            data.append(line)
            line = f.readline()
    return data

nd = get_data(path)

rules = get_rule(nd,minsup=0.8,minconf=0.9)

len(rules)
rules[1]


# In[114]:


def get_rule_test1(data,minsup=0.5,minconf=0.5):
    candi,_ = find_max_freq(data,minsup=minsup)
    
    length = len(candi)
    max_len_item = candi[-1]
    
    for a,b in max_len_item.items():
        for i in range(-length,0-1,1):
            for x,y in candi[i].items():
                if set(x).issubset(set(a)) and b / y>0.5:
                    temp = set(a)-set(x)
                    print("rule:",x,"===>",temp,"conf(a):",b/y)
    return "ok"


# In[115]:


def get_rule_test2(data,minsup=0.5,minconf=0.5):
    candi,_ = find_max_freq(data,minsup=minsup)
    
    length = len(candi)
    max_len_item = candi[-1]
    
    for a,b in max_len_item.items():
        for i in range(-length,0-1,1):
            for x,y in candi[i].items():
                if set(x).issubset(set(a)) and b / y>0.5:
                    temp = set(a)-set(x)
                    print("rule:",x,"===>",temp,"conf(a):",b/y)
    return "ok"

