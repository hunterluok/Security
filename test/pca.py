
# coding: utf-8

# In[14]:


import os
import numpy as np


# In[15]:


os.chdir('/Users/luokui/Documents/机器学习实战/机器学习实战及配套代码/machinelearninginaction/Ch13/')


# In[19]:


ls


# In[108]:


with open('iris.data.txt','r') as f:
    lines = []
    for i in f.readlines():
        line = [j.strip() for j in i.split(',')[:4]]
        #temp = [float(k) for k in line]
        lines.append(line)


# In[115]:


with open('testSet3.txt','r') as f:
    l = f.readlines()


# In[123]:


d = mat(data)*mat(data).T


# In[124]:


d.shape


# In[125]:


from numpy  import *
a,b = np.linalg.eig(d)


# In[127]:


len(a)


# In[129]:


b.shape


# In[135]:


x,y,z= np.linalg.svd(data)

