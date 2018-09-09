
# coding: utf-8

# In[4]:


from numpy import *
import numpy as np


# In[2]:


path = './machinelearninginaction/Ch14/0_5.txt'


# In[18]:


def loadExData():
    return[[1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [1, 1, 1, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1]]
data = loadExData()


# In[15]:


def pd(data,thresd=0.8):
    if isinstance(data,list):
        m = len(data)
        n = len(data[0])
        for i in range(m):
            for j in range(n):
                if  data[i][j]>thresd:
                    print(1,end=' ')
                else:
                    print(0,end=' ')
            print('')        
            
    elif isinstance(data,np.matrixlib.defmatrix.matrix):
        m,n = data.shape
        for i in range(m):
            for j in range(n):
                if  data[i,j]>thresd:
                    print(1,end=' ')
                else:
                    print(0,end=' ')
            print('')
        
    else:
        raise KeyError("Wrong, please wait...")


# In[16]:


def get_data(path):
    data = []
    with open(path,'r') as f:
        line = f.readline()
        while line:
            temp =[]
            line = line.strip()
            for i in range(32):
                temp.append(int(line[i]))
            data.append(temp)
            line = f.readline()
    return data


# In[17]:


def chose_sig(sig,variance,big1=True):
    sums = sum(sig)
    sub_sig = []
    s = 0
    big_1 =[]
    for i in sig:
        s += i
        sub_sig.append(i)
        if s/sums>variance:
            break
    for i in sig:
        if i>=1:
            big_1.append(i)
    
    return sub_sig,s,big_1  


# In[9]:


def restruct_data(data,variance,num=5,ifnum=False):
    s,sigs,v = np.linalg.svd(data)
    sub_sig,loss,big_1 = chose_sig(sigs,variance=variance,big1=True)
    
    if ifnum:
        sub_sig = big_1[:num]
    
    msig = mat(np.diag(sub_sig))
    m,n=msig.shape
    redata = mat(s[:,:m]) * msig * mat(v[:m,:])

    return redata,sub_sig


# In[13]:


#data = get_data(path)
#nd,_ = restruct_data(data,variance=0.8,num=3,ifnum=False)


# In[14]:


import  matplotlib.pylab as plt
#plt.plot(np.arange(len(_)),_,'r')
#plt.plot(np.arange(len(_)),np.repeat(1,9),'b')
#plt.show()


# In[23]:


from numpy import *
data= mat(data)
from numpy import linalg as lg


# In[10]:


def edlidist(x,y):
    x = mat(x)
    y = mat(y)
    temp = lg.norm(x-y)
    return 1./(1+temp)


# In[11]:


def pearsonSim(x,y):
    if len(x)<3:
        return 1.
    else:
        return 0.5 + 0.5 * corrcoef(x,y,rowvar=0)[0][1] # corrcoef 得到的是一个 相关系数矩阵，然后第一行第2个值


# In[92]:


simTotal = 0.
ratsimTotal = 0.

for j in range(n):
    userrating = data[user,j]
    if userrating == 0:
        continue
    overlap = nonzero(logical_and(data[:,3].A>0,data[:,j].A>0))[0]
    overlaps = nonzero(logical_and(data[:,3].A>0,data[:,j].A>0))
    
    print(overlap)
    print(overlaps)
    
    if len(overlap) == 0:
        similarity = 0
    else:
        similarity = edlidist(data[overlap,3],data[overlap,j])
        #print(data[overlap,3])
        #print(similarity)
        #print("***"*10)
        simTotal += similarity
        ratsimTotal += similarity * userrating
        print(userrating)
        print(simTotal)
        print(ratsimTotal)
        print('**'*5)
    
    #if simTotal == 0:
    #    return 0
    #else:
    #    return ratsimTotal/simTotal
    #print(overlap)


# In[67]:


unrateditem = nonzero(data[2,:].A==0)[1]
unrateditem


# In[1]:


def standest(data,user,edlidist,item):
    m,n = data.shape
    simtotal = 0.
    ratsimtotal = 0.
    for i in range(n):
        userrating = data[user,i]
        if userrating == 0:       # 得到该 用户评分不为0的。
            continue
        overlap = nonzero(logical_and(data[:,item].A>0,data[:,i].A>0))[0]
        
        if len(overlap) == 0:
            similarity = 0
        else:
            similarity = edlidist(data[overlap,item],data[overlap,i])
        
        print("the %d and %d similarity is :%f" % (item,i,similarity))
        simtotal += similarity #总相似度，
        ratsimtotal += similarity * userrating #
        
    if simtotal==0.:
        return 0.
    else:
        return ratsimtotal / simtotal # 将评分 规划到  1-5之间。


# In[89]:


def recommend(data,user,n=3,simeans=edlidist,estmethod = sgdest):
    unrateditem = nonzero(data[user,:].A==0)[1] # [1]是取值。
    if len(unrateditem)==0:
        return 'your rated everything'
    itemscores = []
    for item in unrateditem:
        estimatedScore = estmethod(data,user,edlidist,item)
        itemscores.append((item,estimatedScore))
    return sorted(itemscores,key=lambda row:row[1],reverse=True)[:n]


# In[90]:


data


# In[91]:


recommend(data,2,n=2)


# In[32]:


data[0,1]=data[0,0]=data[1,0]=data[2,0]=4


# In[36]:


data=mat([[4,4,0,2,2],[4,0,0,3,3],[4,0,0,1,1],[1,1,1,2,0],[2,2,2,0,0],[1,1,1,0,0],[5,5,5,0,0]])
recommend(data,2,n=3)


# In[37]:


data


# In[41]:


overlap = nonzero(logical_and(data[:,1].A>0,data[:,2].A>0))


# In[42]:


data[overlap]


# In[87]:


def sgdest(data,user,sim,item,varians=0.8):
    data = mat(data)
    m,n = data.shape
    u,sigs,v = linalg.svd(data)
    sums = sum(sigs)
    s = 0.
    for k in range(len(sigs)):
        s +=sigs[k]
        if s / sums > varians:
            new_sigs = mat(diag(sigs[:k]))
            
    formated = data.T * mat(u[:,:4]) * mat(new_sigs.I) # 这里注意对 U 进行变换。
    #return formated
    
    simtotal = 0.
    ratsim = 0.
    
    for i in range(n):
        userrating = data[user,i]
        if userrating==0 and i==item:
            continue
        similarity = sim(formated[item,:],formated[i,:])
        
        print("item = %d and %d similarity is :%f" %(item,i,similarity))
        simtotal += similarity
        ratsim += similarity * userrating
        if simtotal == 0:
            return 0
        else:
            return ratsim/simtotal


# In[88]:


sgdest(data=data,user=2,item=3,sim=edlidist)


# In[59]:




