#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, tan, log, log10

function = input("Please enter the function you want to integrate: ")
u = eval(input("Please enter the upper bound: "))
l = eval(input("Please enter the lower bound: "))
x = np.random.uniform(low=l, high=u, size=1000)
y=eval(function)
int = sum(y)*(u-l)/1000
print(int)


# In[ ]:




