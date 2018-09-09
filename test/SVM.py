
# coding: utf-8

# In[6]:


import numpy as np


# In[44]:


from numpy import *


# In[36]:


def loaddataset(filename):
    datamat =[];label=[]
    fr = open(filename)
    for line in fr.readlines():
        linearr = line.strip().split('\t')
        datamat.append([float(linearr[0]),float(linearr[1])])
        label.append(float(linearr[2]))
    return datamat,label


# In[40]:


data,label = loaddataset(path)


# In[8]:


def selectJrand(i,m):
    if i>m:
        #raise ValueError("The i: %d must smaller than m"%(i))
        raise ValueError("The i: {} must smaller than m".format(i))
    j = i
    while j==i:
        j = int(np.random.uniform(0,m))
    return j

def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    elif aj < L:
        aj = L
    else:
        pass
    return aj


# In[66]:


def smosimple(dataMatIn,classLabels,C,toler,MaxIter):
    dataMatrix = mat(dataMatIn);
    labelMat = mat(classLabels).transpose()
    b = 0
    m,n=shape(dataMatIn)
    alphas = mat(zeros((m,1)))
    iters =0
    while (iters<MaxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fxi = float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T))+b
            Ei = fxi - float(labelMat[i])
            if((labelMat[i]*Ei<-toler) and (alphas[i]<C)) or ((labelMat[i]*Ei>toler and (alphas[i]<C))):
                j = selectJrand(i,m)
                fxj = float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T))+b
                Ej =fxj-float(labelMat[j])
               
            # 复制 以备用。
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                                             
                if (labelMat[i]!=labelMat[j]):
                    L = max(0,alphas[j]-alphas[i])
                    H = min(C,C+alphas[j]-alphas[i])
                else:
                    L = max(0,alphas[j]+alphas[i]-C)
                    H = min(C,alphas[j]+alphas[i])
                if L==H:
                    print("L==H")
                    continue
               
            # 计算eta 用来更新alpha
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T-dataMatrix[i,:]*dataMatrix[i,:].T-                                                             dataMatrix[j,:] * dataMatrix[j,:].T
               
                if eta>=0:
                    print("eta>=0")
                    continue
               
            # 更新 alphas [j]
                alphas[j] -= labelMat[j] *(Ei-Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
               
                if (abs(alphas[j]-alphaJold)<0.00001):
                    print("j not moving enough")
                    continue
                   
            # 更新 alphas [i]
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold-alphas[j])
               
            # 更新 b 两个  不满足条件 就求均值。
                b1 = b - Ei - labelMat[i] * (alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T-                labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
               
                b2 = b - Ej - labelMat[i] * (alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T-                labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
               
                if (0<alphas[i]) and (C>alphas[i]):
                    b = b1
                elif (0<alphas[j]) and (C>alphas[j]):
                    b = b2
                else:
                    b = (b1+b2)/2.
                
            
                alphaPairsChanged +=1
                print("iterL%d i :%d,pairs changed %d" %(iters,i,alphaPairsChanged))
               
        if (alphaPairsChanged==0):
            iters +=1
        else:
            iters =0
        print("iteration number :%d" % iters)
    return b,alphas           


# In[10]:


import os 
path = '/Users/luokui/Documents/机器学习实战/机器学习实战及配套代码/machinelearninginaction/Ch06/testSet.txt'


# In[42]:


"""
label = []
data = []
with open(path,'r') as f:
    line = f.readline().strip().split('\t')
    print(line)
    while line:
        temp = [i for i in line[:2]]
        temp_label = [i for i in line[2:3]]
        data.append(temp)
        label.append(temp_label)
        line = f.readline().strip().split('\t')
"""


# In[67]:


b,alphas = smosimple(data,label,0.6,0.001,40)


# In[63]:


b


# In[64]:


alphas[alphas>0]


# In[65]:


for i in range(100):
    if alphas[i]>0:
        print(data[i])


# In[83]:


a =np.mat(np.ones((4,2)))


# In[84]:


a[0]=0


# In[85]:


a[3]=0


# In[86]:


a[:,0]


# In[76]:


a= np.array(a)


# In[89]:


nonzero(a[:,0].A)[0]

