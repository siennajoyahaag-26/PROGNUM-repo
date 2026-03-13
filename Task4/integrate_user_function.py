#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy import sin, cos, exp, pi
import scipy
fun = input("Please enter the function you wish to integrate over: ")
def a(x):
        return eval(fun)
try:
    int, e = scipy.integrate.quad(a, 0, pi)
    print(int)
    x = np.random.uniform(low=0, high=pi, size=1000)
    y=eval(fun)
    int2 = sum(y)*(pi-0)/1000
    print(int2)
except NameError:
    print("Make sure you are using x as your variable. If you already are, then the function you have entered is not defined. I can't integrate it for you. ")
except TypeError:
    print("Please use x as your variable.")
except SyntaxError:
    print("Double check your syntax.")
except ZeroDivisionError:
    print("This integral is undefined, as it requires division by 0.")


# In[ ]:




