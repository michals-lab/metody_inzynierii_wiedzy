# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:41:22 2022

@author: michal
"""

import random


def monte_carlo(n,x_p,x_k,y_p,y_k):
    p = (abs(y_k-y_p)*abs(x_k-x_p))
    u = lambda x: x
    pod = 0
    for r in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if y < u(x):
            pod += 1
    integral = p* (pod/n)
    print("monte carlo =>",integral)
    
def integral_square(n, x_p, x_k):
    d_x = ((x_k - x_p)/n)
    u = lambda x: x**2
    res = 0
    for i in range(n):
        res += u(x_p + i * d_x) * d_x
    print("square =>",res)


    
monte_carlo(1000,0,1,0,1)
integral_square(1000, 0, 1)