
# coding: utf-8

# In[1]:


from numpy import *


# In[4]:


paths='/Users/luokui/Documents/机器学习实战/机器学习实战及配套代码/machinelearninginaction/Ch10/testSet.txt'

def get_data(paths):
    data = []
    with open(paths,'r') as f:
        fr = f.readlines()
        for line in fr:
            line = line.strip().split('\t')
            temp = [float(i) for i in line]
            data.append(temp)   
    return mat(data)
data = get_data(paths)


# In[52]:


def cal_dist(centers,data,k):
    data= mat(data)
    m,n = data.shape
    dists = zeros((m,k))
    for j in range(k):
        for i in range(m):
            dists[i,j] = sqrt(sum(pow((centers-data[i]).A,2)))
    return dists


# In[31]:


def chose_center(data,k):
    ids = []
    m,n = data.shape
    indexs =list(arange(m))
    for i in range(k):
        NL = len(indexs)
        index = random.randint(0,NL,1)[0]  # 这个地方需要注意啊 ，
        ids.append(indexs[index])
        indexs.remove(indexs[index])
    centers = data[ids]
    return centers
cen = chose_center(data,5)


# In[53]:


dists = cal_dist(cen,data,5)


# In[58]:


dists.argmax(0)


# In[60]:


dists.shape

