
# coding: utf-8

# In[1]:


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
              #[1,1,'maybe']]
    labels = ['no surfacing','flippers']
    return dataSet, labels


# In[2]:


import numpy as np
np.log2(4)


# In[3]:


data,label = createDataSet()
print(data)
label


# In[4]:


def cal(data): 
    cout_dic ={}
    m = len(data)
    for i in range(m):
        temp = data[i][-1]
        cout_dic.setdefault(temp,0)
        cout_dic[temp] +=1
    cout_dic = {k:-(v/m)*(np.log2(v/m)) for k,v in cout_dic.items()}
    entrop = sum(cout_dic.values())
    return entrop

cal(data)


# In[5]:


def gini(data):
    cout_dic ={}
    m = len(data)
    for i in range(m):
        temp = data[i][-1]
        cout_dic.setdefault(temp,0)
        cout_dic[temp] +=1
    cout_dic = {k:(v/m)**2 for k,v in cout_dic.items()}
    gini = 1- sum(cout_dic.values())
    return gini,cout_dic
gini(data)


# In[6]:


def split_feature(data,k=0):
    m = len(data)
    #n = len(data[0])
    data = np.array(data)
    t = np.unique(data[:,k])
    splitdata={}
    for i in t:
        for j in range(m):
            if data[j,k]==i:
                splitdata.setdefault(i,[])
                splitdata[i].append(data[j])
    return splitdata


# In[7]:


data


# In[8]:


xx = split_feature(data,0)
xx


# In[9]:


new_entrop=0.
for key,value in xx.items():
    length =len(value)
    new_entrop +=length/5 *cal(value)
    #new_entrop +=cal(value)
    print(new_entrop)


# In[10]:


cal(data)-new_entrop


# In[11]:


# 选择最优的分裂的枝叶。
def chose_best_feature(data):
    old_entrop = cal(data)
    n = len(data[0])-1
    entrop_change = {}
    len_data = len(data)
    
    for i in range(n):
        temp = split_feature(data,k=i)
        new_entrop = 0.
        for key,value in temp.items():
            length =len(value)
            new_entrop +=length/len_data *cal(value) #这里注意用法。
        entrop_change.setdefault(i,0)
        entrop_change[i]= old_entrop-new_entrop
    sort_entrop_change = sorted(entrop_change.items(),key=lambda row:row[1],reverse=True)
    best_feature =sort_entrop_change[0][0]
    return sort_entrop_change,best_feature


# In[13]:


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        classCount.setDefault(vote,0)
        classCount[vote] +=1
    sort = sorted(classCount.items(),key=lambda row:row[1],reverse=True)
    return sort[0][0]


# In[14]:


def split_feature_x(data,axis,value):
    splitdata=[]
    for vect in data:
        if vect[axis]==value:
            temp = vect[:axis]
            temp.extend(vect[axis+1:])
            splitdata.append(temp)
    return splitdata
split_feature_x(data,0,1)


# In[27]:


def createTree(dataset,labels):
    classList = [ example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0])==1:
        return majorityCnt(classList)
    _,bestFeat = chose_best_feature(dataset)
    bestFeatLabel = labels[bestFeat]
    
    myTree ={bestFeatLabel:{}}
    del labels[bestFeat]
    
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value]=createTree(split_feature_x(
        dataset,bestFeat,value),subLabels)
    return myTree


# In[28]:


a = [1,2,3,2]


# In[32]:


data
label


# In[85]:


data,label = createDataSet()
t = createTree(data,label)
fir =[i for i in t.keys()][0]

#fir =np.array(t.keys())
fir
#sd = t[fir]
#sd


# In[89]:


data,labels = createDataSet()
labels


# In[97]:


firstStr = [i for i in t.keys()][0]
secondDict = t[firstStr]
featIndex = labels.index(firstStr)
featIndex
secondDict.keys()


# In[98]:


def classify(inputTree,featLabels,testVec):
    firstStr = [i for i in inputTree.keys()][0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    
    for key in secondDict.keys():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=='dict':
                classLabel = classify(secondDict[key],featLabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


# In[99]:


data,labels = createDataSet()
mytree = createTree(data,labels)
classify(mytree,labels,[1,0])


# In[57]:


mytree#.keys()


# In[60]:


for i in mytree.keys():
    print(i)
    print(mytree[i])


# In[66]:


def storetree(putTree,filename):
    import pickle
    fw = open(filename,'wb')
    pickle.dump(putTree,fw)
    fw.close()
    
def loadtree(filename):
    import pickle
    fr = open(filename,'rb')
    return pickle.load(fr)

storetree(createTree,'./filetree.txt')

m = loadtree('./filetree.txt')

data,labels = createDataSet()
m(data,labels)

