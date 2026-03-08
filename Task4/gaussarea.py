#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

# User inputs for all of the values and the integration bounds
print("Please enter:")
A = float(input("the amplitude: "))
x0 = float(input("where you want the peak to be: "))
sigma = float(input("the width of the peak: "))
z0 = float(input("the offset in y: "))
a = float(input("the lower bound for the integration: "))
b = float(input("the upper bound for the integration: "))

x = np.linspace((-4*sigma)+x0,4*sigma+x0,200) # Data for plot that encompasses most of the curve and is centered at x0
f = gauss(x, A, x0, sigma, z0) # Calculating corresponding y values using the gauss function
plt.plot(x, f)

x1 = np.linspace(a, b, 200) # Data for shaded region using limits provided by user
f1 = gauss(x1, A, x0, sigma, z0) # Calculating corresponding y values using the gauss function
area, ae = sp.integrate.quad(gauss, a, b, args = (A, x0, sigma, z0)) # Calculating the area and seperating it from the error provided
plt.fill_between(x1, f1, z0, label = f"The area of the shaded region is {area: .2f}") # Filling the area indicated by the bounds and adding the appropriate label for the legend

plt.legend(loc='upper right')
plt.show()


# ![gaussarea1.png](attachment:a741a551-7a47-4026-89af-a254cee31980.png)

# In[ ]:




