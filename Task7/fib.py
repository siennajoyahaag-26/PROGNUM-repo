#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        
    def nth(self):
        i = 0
        b = 1
        a = 0
        Nth = 0
        while i < self.N :
            Nth = a + b
            a = b
            b = Nth
            i = i + 1
        return Nth
    
    def divM(self):
        allF = []
        Nth = 0
        j = 0
        b = 1
        a = 0
        Nth = 0
        while j < self.N :
            Nth = a + b
            a = b
            b = Nth
            if Nth%self.M == 0:
                allF.append(Nth)
            j = j + 1
        return allF
fib = Fibonacci(100, 7)
print(fib.nth())
print(fib.divM())

