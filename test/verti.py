
# coding: utf-8

# In[25]:


from numpy import *


# In[26]:


A  = matrix([[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]])
#A  = matrix([[0.5,0.3,0.2],[0.3,0.2,0.5],[0.2,0.5,0.3]])
B = matrix([[0.5,0.5],[0.4,0.6],[0.7,0.3]])
pi = matrix([0.2,0.4,0.4]).T


# In[27]:


print(A,'\n',B,'\n',pi)


# In[28]:


o = ['1','0','1']


# In[29]:


for i in range(len(o)):
    if o[i]=='1' and i==0:
        t1 = multiply(B[:,0],pi)
        print("初始转移矩阵的值 \n{},\n{}\n".format(t1,'^'*10))
    
    if o[i]=='0':
        inter_temp = []
        for j in range(3):
            temp = multiply(t1,A[:,j])
            temp = max(temp) * B[j,1]
            inter_temp.append(temp.tolist()[0]) # 使得矩阵的维度 为2维的
            #print("**"*10)
        print(inter_temp)
        
    if o[i]=='1'and i!=0:
        inter_temp2 = []
        for j in range(3):
            temp = multiply(inter_temp,A[:,j])
            temp = max(temp) * B[j,0]
            inter_temp2.append(temp.tolist()[0]) # 使得矩阵的维度 为2维的
            #print("**"*10)
        print(inter_temp2)
        


# In[64]:


m,n = A.shape
resu ={}

for i in range(len(o)):
    if o[i]=='1' and i==0:
        tes = multiply(B[:,0],pi)
        print("初始转移矩阵的值 \n{},\n{}\n".format(tes,'^'*10))
        print('*'*10)
        resu.setdefault(i,tes.argmax()+1)
    
    else:
        temp_dir = {}
        inter_temp = []
        
        for j in range(n):
            temp = multiply(tes,A[:,j])
            
            max_value = max(temp)  
            temp_dir.setdefault(temp.argmax()+1,max_value)
            
            if o[i]=='0':
                temp = max_value * B[j,1]
            else:
                temp = max_value * B[j,0]
            inter_temp.append(temp.tolist()[0]) # 使得矩阵的维度 为2维的
        
        temp_dir = sorted(temp_dir.items(),key=lambda row:row[1],reverse=True)
        
        resu.setdefault(i,temp_dir[0][0])  
        tes = inter_temp
        
        print(tes,'*'*10)


# In[98]:


def verbi_algorith(A,B,pi,o):
    m,n = A.shape
    resu ={}
    re_p = []
    
    for i in range(len(o)):
        if o[i]=='1' and i==0:
            tes = multiply(B[:,0],pi)
            #print("初始转移矩阵的值 \n{},\n{}\n".format(tes,'^'*10))
            #print('*'*10)
            
            resu.setdefault(i+1,tes.argmax()+1)
            re_p.append(tes)
    
        else:
            temp_dir = {}
            inter_temp = []
        
            for j in range(n):
                temp = multiply(tes,A[:,j])
            
                max_value = max(temp)  
                temp_dir.setdefault(temp.argmax()+1,max_value)
            
                if o[i]=='0':
                    temp = max_value * B[j,1]
                else:
                    temp = max_value * B[j,0]
                inter_temp.append(temp.tolist()[0]) # 使得矩阵的维度 为2维的
                
            tes = inter_temp
            re_p.append(tes)
        
            temp_dir = sorted(temp_dir.items(),key=lambda row:row[1],reverse=True)
            resu.setdefault(i+1,temp_dir[0][0])  
            
    return resu,re_p


# In[92]:


A


# In[93]:


B


# In[94]:


pi


# In[95]:


o1 = ['1','0','1','0']
o2 = ['1','0','1','1','0','1','0','0']


# In[99]:


verbi_algorith(A,B,pi,o)


# In[97]:


verbi_algorith(A,B,pi,o1)


# In[68]:


o

