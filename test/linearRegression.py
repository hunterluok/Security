
# coding: utf-8

# #（1） 正规方程组

# In[ ]:


import numpy as np
from numpy import *
x = np.arange(20).reshape(10,2)
y = np.random.rand(10,1) +np.matmul(x,[[2],[1]])

def linear(x,y):
    x = mat(x);y=mat(y) # 如果不mat的 话 *就是不能进行矩阵的乘法。而是逐元乘积
    xtx = (x.T * x).I
    w  = xtx * x.T *y
    y_pred = x*w
    loss = np.mean(np.array((y_pred-y))**2)
    return np.array(y_pred),loss
    

y_pred,loss = linear(x,y)

# t = np.array((y - x * (mat(x.T)*mat(x)).I * x.T * y))**2
import matplotlib.pyplot as plt
plt.plot(np.arange(len(y_pred)),y_pred,color="red")
plt.plot(np.arange(len(y_pred)),np.array(y).flatten(),color='black') # 将np.array()进行flatten 就不是矩阵了
plt.show()


# # (2) local weight linear regression

# In[ ]:


def lwlr(test,x,y,k):
    x = mat(x);y =mat(y);mat(test)
    m,n = x.shape
    w = mat(eye(m))
    
    for i in range(m):
        diff = test-x[i]
        w[i,i] = exp(-(diff * diff.T)/(2.*k**2))
    
    xtx = (x.T * w * x).I
    w = xtx * (x.T * w) * y
    y_pred = x * w
    
    loss = np.mean(np.array((y_pred-y))**2)
    return y_pred,loss

lwlr(mat([1,2]),x,y,0.1)


# In[2]:


# (3) rigde regression


# In[ ]:


import numpy as np
from numpy import *
x = np.arange(20).reshape(10,2)
y = np.random.rand(10,1) +np.matmul(x,[[2],[1]])

def linear(x,y,lam=0.2):
    x = mat(x);y=mat(y) # 如果不mat的 话 *就是不能进行矩阵的乘法。而是逐元乘积
    xtx = (x.T * x + lam * mat(eye(x.shape[1]))).I
    w  = xtx * x.T *y
    y_pred = x*w
    loss = np.mean(np.array((y_pred-y))**2)
    return np.array(y_pred),loss
    

y_pred,loss = linear(x,y)

# t = np.array((y - x * (mat(x.T)*mat(x)).I * x.T * y))**2
import matplotlib.pyplot as plt
plt.plot(np.arange(len(y_pred)),y_pred,color="red")
plt.plot(np.arange(len(y_pred)),np.array(y).flatten(),color='black')
plt.show()


# In[3]:


#(4) forward stagewise linear regression


# In[ ]:


import numpy as np
from numpy import *
x = np.arange(20).reshape(10,2)
y = np.random.rand(10,1) +np.matmul(x,[[2],[1]])

def cost(y_pred,y):
    return np.mean(np.array((y_pred-y))**2)

def linear(x,y,iters=10,eps=0.01):
    x = mat(x);y=mat(y)
    m,n = x.shape
    #w = mat(ones(n)).T
    w = zeros((n,1))
    wtest = w.copy()
    wmax = w.copy()
    
    for i in range(iters):
        losses = inf
        for j in range(n):
            for sign in [-1,1]:
                wtest = w.copy()
                wtest[j] += sign*eps
                y_pred = x *w
                loss =cost(y_pred,y)
                if loss<losses:
                    losses =loss
                    wmax = wtest
        w = wmax.copy()
        
    y_pred = x * w
    return y_pred
    

y_pred = linear(x,y,iters=1000)

# t = np.array((y - x * (mat(x.T)*mat(x)).I * x.T * y))**2
import matplotlib.pyplot as plt
plt.plot(np.arange(len(y_pred)),y_pred,color="red")
plt.plot(np.arange(len(y_pred)),np.array(y).flatten(),color='black')
plt.show()

