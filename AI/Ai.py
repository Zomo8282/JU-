#!/usr/bin/env python
# coding: utf-8

# In[66]:


x=input("enter string from a-e with 5 letters without repetition")
s={"ba":0,"ca":0,"da":0,"ea":0,"cb":0,"db":0,"eb":0,"dc":0,"ec":0,"ed":0}
l=""
if x!="abcde":
        l=x
        for i in s :
            if i in x:
                s[i]=1
                l= x.replace(i,i[::-1])
                x=l
        print(s)
        print(l)
        print(iiteration)
                    
        


# In[ ]:





# In[ ]:




