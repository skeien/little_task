# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:55:43 2022

@author: sebas
"""

import numpy as np

#Hill-climbing parabolic function
#%%
dt=0.5
array = np.arange(-5, 5+dt, dt)
for i in range(len(array)):
    array[i] = 2-array[i]**2
maxv =-float('inf')
i=0

while maxv <= array[i]:
    maxv = array[i]
    posv = i
    if i <  len(array):
        i+=1
    else:
        break
print(posv)
print(maxv)
#%%
import random

dt=0.5
array = np.arange(0, 10+dt, dt)
a=0.0051
b=-0.1367
c=1.24
d=-4.456
e=5.66
f=-0.287
for i in range(len(array)):
    array[i] = a*array[i]**5+b*array[i]**4+c*array[i]**3+d*array[i]**2+e*array[i]+f
times=20
for i in range(times):
    i = random.randrange(0, len(array))
    maxv = array[i]
    posv = i
    if posv <len(array)-1:
        if array[i+1]>array[i-1]:
            while maxv <= array[i]:
                maxv = array[i]
                posv = i
                if i <  len(array):
                    i+=1
                else:
                    break
        else:
            while maxv <= array[i]:
                maxv = array[i]
                posv = i
                i-=1
                # if i ==0: #Not necessary in python
                #     break
    print(posv)
    print(maxv)

