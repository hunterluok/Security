
# coding: utf-8

# In[1]:


from numpy import *


# In[2]:


def pred_value(data,dim,threadvalue,thread_dirct):
    m,n = data.shape
    preds = ones((m,1))
    if thread_dirct =='lt':
        preds[data[:,dim] <= threadvalue] = -1.0
    else:
        preds[data[:,dim] > threadvalue] = -1.0
    return preds


# In[3]:


def loadSimpData():
    datMat = matrix([[ 1. ,  2.1],[ 2. , 1.1], [ 1.3, 1. ], [1., 1.], [2., 1.]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat,classLabels

data,label = loadSimpData()


# In[4]:


def adaboost_model(data,label,D,N=10.0):
    m,n = mat(data).shape
    label = matrix(label).T
    numsteps = N
    beststump = {}
    minerr = inf
    
    for i in range(n):
        minvalue, maxvalue = data[:,i].min(),data[:,i].max()
        step = (maxvalue-minvalue) / numsteps
        #print(step)
        for j in range(-1,int(numsteps)+1):
            for k in ['lt','rh']:
                threadvalues = minvalue + j * step
                preds = pred_value(data,i,threadvalues,k)
                
                errarr = mat(ones((m,1)))
                errarr[preds == label]=0 # 构造一个误差矩阵，当不相等时 为1 否则为1。

                weight_err = mat(D).T *errarr
                #print("dim={},weighterr={},thread={},dir={}".format(i,weight_err,threadvalues,k))
                
                if weight_err<minerr:
                    minerr = weight_err
                    beststump['bestclass'] = preds #.copy()
                    beststump['best_dim'] = i
                    beststump['best_threadvalue'] = threadvalues
                    beststump['best_dir'] = k
                    beststump['min_err'] = minerr
                    #print("best_dim={},minerr={},best_thread={},best_dir={}".format(i,minerr,threadvalue,k))
    return beststump


# In[5]:


#perd_err = 1-sum(pred_value(data,dim=0,threadvalue=1.3,thread_dirct='lt')==mat(label).T)/5
#round(perd_err,2)
#print("pred_err={:.2f}".format(perd_err))


# In[7]:


#fx = adaboost_model(data,label,d,10)


# In[9]:


#preds = fx['bestclass']
#multiply(mat(label).T,preds)
#print(preds)


# In[49]:


def f(data,label,iters=10,N=10.): # iters 决定弱分类器的个数
    m,n = mat(data).shape
    D = ones((m,1))/m
    model_agg = []
    aggclassest = mat(zeros((m,1)))
    
    if mat(label).shape[0] !=m:
        label = mat(label)
    else:
        label = mat(label).T
    if label.shape[0] ==m:
        raise KeyError("The dim of label is wrong")
    
    for i in range(iters):
        bestmodel = adaboost_model(data,label,D,10)
        model_agg.append(bestmodel)
        
        err = bestmodel['min_err']
        alpha = 0.5* log((1.0-err)/max(err,1e-16))
        bestmodel['alphas'] = alpha
    
        preds = bestmodel['bestclass']
        if preds.shape[0]!=m:
            preds = preds.T
            
        temp = -1 * multiply(multiply(alpha,mat(label).T),preds)
        D = multiply(D,exp(temp))/sum(D)
        
        aggclassest += multiply(alpha,preds)
        #print("aggclassset :",aggclassest)
        
        aggerrors = multiply(sign(aggclassest)!=mat(label).T,ones((m,1)))
        errrate = aggerrors.sum() / m
        if errstate ==0:
            break
        
    return model_agg,aggclassest


# In[11]:


#m = f(data,5,label)


# In[27]:


def adaclassify(data,classifierArr,label):
    data = mat(data)
    m = data.shape[0]
    aggclassset = mat(zeros((m,1)))
    for i in range(len(classifierArr)):
        preds = pred_value(data,classifierArr[i]['best_dim'],classifierArr[i]['best_threadvalue'],classifierArr[i]['best_dir'])
        aggclassset += multiply(classifierArr[i]['alphas'],preds)
        #print(aggclassset)
    last_pred = sign(aggclassset)
    err = sum((last_pred!=mat(label).T))/m
    
    return aggclassset,last_pred,err


# In[28]:


#adaclassify(data,m,label)


# In[29]:


trainp = '/Users/luokui/Documents/机器学习实战/机器学习实战及配套代码/machinelearninginaction/Ch07/horseColicTraining2.txt'


# In[30]:


testp = '/Users/luokui/Documents/机器学习实战/机器学习实战及配套代码/machinelearninginaction/Ch07/horseColicTest2.txt'


# In[31]:


def loaddata(path):
    nfeat = len(open(trainp).readline().strip().split('\t'))
    data = []
    label = []
    fr = open(path)
    for line in fr.readlines():
        lines = []
        curline = line.strip().split('\t')
        for i in range(nfeat-1):
            lines.append(float(curline[i]))
        data.append(lines)
        label.append(float(curline[-1]))
    return array(data),array(label)


# In[32]:


td,tl = loaddata(trainp)
testt,testl=loaddata(testp)


# In[20]:


#adaboost_model(data,10,label)
models = f(td,10,tl)


# In[22]:


a,b=adaclassify(testt,models,testl)


# In[38]:


re={}
for i in [1,10,50,100]:
    models = f(td,i,tl)
    agg_pred,last_pred,b = adaclassify(testt,models,testl)
    re.setdefault('agg_preds',[])
    re.setdefault('last_preds',[])
    re.setdefault('errs',[])
    re['agg_preds'].append(agg_pred)
    re['last_preds'].append(last_pred)
    re['errs'].append(b)


# In[163]:


def plot_roc(preds,classlabels):
    import matplotlib.pyplot as plt
    cur = (1.0,1.0)
    ySum = 0.
    numPosClas = sum(array(classlabels)==1.0)
    yStep = 1/float(numPosClas)
    xStep = 1/float(len(classlabels)-numPosClas)
    
    temps = preds.A.reshape(-1)
    sortedindices = temps.argsort()
    
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(1,1,1)
    
    for index in sortedindices:
        if classlabels[index]==1.0:
            delX = 0
            delY = yStep
        else:
            delX = xStep
            delY = 0
            ySum += cur[1]
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY],c='r')
        cur = (cur[0]-delX,cur[1]-delY)
    ax.plot([0,1],[0,1],'b--')
    ax.axis([0,1,0,1])
    plt.show()
    print("the area under the cureve is :",ySum * xStep)

modelss,predss = f(td,tl)
plot_roc(predss,tl)


# In[139]:


#temp = predss.A.reshape(-1)
#xx = temp.argsort()


# In[165]:


import matplotlib.pyplot as plt
cur = (1.0,1.0)
ySum = 0.
numPosClas = sum(array(tl)==1.0)
yStep = 1/float(numPosClas)
xStep = 1/float(len(tl)-numPosClas)
    
temps = predss.A.reshape(-1)
sds = temps.argsort()
    
fig = plt.figure(figsize=(12,8))
fig.clf()
ax = plt.subplot(1,1,1)
    
for index in sds:
    #print(index)
    if tl[index]==1.0:
        delX = 0
        delY = yStep
    else:
        delX = xStep
        delY = 0
        ySum += cur[1]
    ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY],c='r')
    cur = (cur[0]-delX,cur[1]-delY)
ax.plot([0,1],[0,1],'b--')
ax.axis([0,1,0,1])
plt.show()
print("the area under the cureve is :",ySum * xStep)

