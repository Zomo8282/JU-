#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
def gram_schmidt(a):
    q = []
    for i in range(len(a)):
        #orthogonalization
        q_tilde = a[i]
        for j in range(len(q)):
            q_tilde = q_tilde - (q[j] @ a[i])*q[j]
        #Test for dependennce
        if np.sqrt(sum(q_tilde**2)) <= 1e-10:
            print("Vectors are linearly dependent.")
            print("GS algorithm terminates at iteration ", i+1)
            return q
        #Normalization
        else:
            q_tilde = q_tilde / np.sqrt(sum(q_tilde**2))
            q.append(q_tilde)
    print("Vectors are linearly independent.")
    return q
    
a=np.array([(1,-2,1,-1),(1,1,3,-1),(-3,7,1,3)])
q=gram_schmidt(a)
print(q)
#Test orthonormality
print("Norm of q[0] :", (sum(q[0]**2))**0.5)
print('Inner product of q[0] and q[1] :', q[0] @ q[1])
print("Inner product of q[0] and q[2] :", q[0] @ q[2])
print("Norm of q[1] :", (sum(q[1]**2))**0.5)
print("Inner product of q[1] and q[2] :", q[1] @ q[2])
print("Norm of q[2] :", (sum(q[2]**2))**0.5) 


# In[ ]:




