#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
u= input("Are you ready to play rock, paper, scissors? Please enter R (rock), P (paper) or S (scissors) to begin: ") # Takes user input as their choice.
if type(u)!= str or len(u)!=1: # Checks that the input is a string and is only one letter.
    u = input("Please enter only the first letter: ") # Error message
rps=np.random.randint(1, 3+1) # Creating a random integer between 1 and 3

# Assigning either R, P, or S, depending on the random integer.
if rps==1: 
    g="R"
elif rps==2:
    g="S"
else:
    g="P"
# Comparing input and computer's generation to see who wins, and printing the result.
if g==u:
    print(f"It's a tie! The computer also chose {g}.")
elif (u=="S" and g=="R") or (u=="R" and g=="P") or (u=="P" and g=="S"):
        print(f"Computer wins! It chose {g}.")
elif (u=="R" and g=="S") or (u=="P" and g=="R") or (u=="S" and g=="P"):
        print(f"You win! The computer chose {g}.")
else:
    print("Something went wrong. Please make sure you enter either P, R or S.") # Error message in case they put a different letter


# In[ ]:




