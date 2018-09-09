
# coding: utf-8

# In[1]:


class treeNode:
    def __init__(self,nameValue,numOccur,parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}
        
    def inc(self,numOccur):
        self.count += numOccur
        
    def disp(self,ind=1):
        print(' '*ind,self.name,' ',self.count)
        for child in self.children.values():
            child.disp(ind+1)


# In[4]:


rootnode = treeNode('pyramid',9,None)


# In[5]:


rootnode.children['eye'] = treeNode('eye',13,None)


# In[6]:


rootnode.disp()


# In[9]:


rootnode.children['phoenix'] =treeNode('phoenix',3,None)
rootnode.children['hbase'] =treeNode('hbase',10,None)


# In[10]:


rootnode.disp()


# In[13]:


def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['Z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict


# In[14]:


redDict= createInitSet(loadSimpDat())
redDict


# In[16]:


for a,b in redDict.items():
    print(a,b)

