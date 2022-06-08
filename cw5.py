# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 20:03:39 2022

@author: michal
"""
import numpy as np
import math

def dot_prod(v1,v2):
    v3=0
    for i in range(len(v1)):
        v3 += v1[i]*v2[i]
    return v3

# srednia el wektora 
def average(v1):
    l = len(v1)
    return dot_prod(v1, np.ones(l))/l

# oblicza waraincje el wektora
def variance(v1):
    l = len(v1)
    sr = average(v1)
    x =v1 -(np.ones(l) * sr)
    return dot_prod(x, x)/l

# odchylenie 
def std_deviation(v1):
    return math.sqrt(variance(v1))

x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y = np.array([1,3])
z = [1,2]

print("srednia y=>",average(y))
print("wariancja x=>",variance(x))
print("wariancja y=>",variance(y))
print("wariancja z=>",variance(z))
print("odchylenie =>",std_deviation(y))

