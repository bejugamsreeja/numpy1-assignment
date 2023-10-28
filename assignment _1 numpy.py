#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1. Create a null vector of size 10 but the fifth value which is 1.

import numpy as np 
x=np.zeros(10)
x[4]=1
print(x)


# In[13]:


#2. Create a vector with values ranging from 10 to 49.

import numpy as np 
x = np.arange(10,50)
print(x)


# In[14]:


#3. Create a 3x3 matrix with values ranging from 0 to 8

import numpy as np
x = np.arange(9).reshape(3,3)
print(x)
        


# In[15]:


#4. Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np
x = np.nonzero([1,2,0,0,4,0])
print(x)
        


# In[16]:


#5. Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np
X = np.random.random((10,10))
Xmin, Xmax = X.min(), X.max()
print(Xmin, Xmax)
        


# In[17]:


#6. Create a random vector of size 30 and find the mean value.
import numpy as np
X = np.random.random(30)
m = X.mean()
print(m)


# In[ ]:




