# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:18:47 2022

@author: michal
"""

import numpy as np
import math

def dot_prod(v1,v2):
    v3=0
    for i in range(len(v1)):
        v3 += v1[i]*v2[i]
    return v3

def proj(u, v):
    return (np.dot(v,u) / np.dot(u,u)) * u

def len_v(v):
    return math.sqrt(dot_prod(v,v))

def q_r(matrix):
    matrix = np.transpose(matrix)
    q, u_list = [], [matrix[0]]
    e = np.array(u_list[0]) / len_v(u_list[0])
    q.append(e)

    for x in range(1, len(matrix)):
        u = matrix[x]
        for y in range(len(u_list)):
            u = u - proj(u_list[y], matrix[x])
        u_list.append(u)
        e = u / len_v(u)
        q.append(e)

    r = np.dot(q, np.transpose(matrix))
    q = np.transpose(q)
    return (q, r)

        
x = [[1,0,2],[1,0,2]]        
print(q_r(x))
