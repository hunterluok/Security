
# coding: utf-8

# In[ ]:


# 利用词袋模型。
def train(x,y):
    numtraindocs = len(x)
    numwords = len(x[0])
    pri = sum(y)/float(numtraindocs)
    
    ponum = ones(numwords);p1num = ones(numwords) #初始化为1，2防止分母为0
    podem = 2.0; p1dem=2.
    for i in range(numtraindocs):
        if y[i]==1:
            p1num +=x[i]
            p1dem += sum(x[i])
        else:
            ponum +=x[i]
            podem +=sum(x[i])
    p1vec = p1num/p1dem
    povec = ponum/podem
    return log(p1vec),log(povec),pri #注意这里的取对数

def model(test,plvec,povec,pri):
    p1 = sum(test*p1vec)+log(pri)
    p0 = sum(test*povec)+log(pri)
    if p1>p0:
        return 1
    else:
        return 0

p1vec,povec,pri = train(nd,label)
model(thisDoc,p1vec,povec,pri)

