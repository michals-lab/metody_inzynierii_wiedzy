# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 18:08:33 2022

@author: michal
"""

import numpy as np

def covariance(matrix):
    return np.dot(matrix.T,matrix)

def invert(matrix):
    return np.linalg.inv(matrix)

def inv_left(matrix):
    cov = covariance(matrix)
    inv = invert(cov)
    return np.dot(inv,matrix.T)
  
def linear_reg(matrix):
    matrix_x=np.array([[1,x[0]]for x in matrix])
    matrix_y=np.array([x[1]for x in matrix])
    invL = inv_left(matrix_x)
    return np.dot(invL,matrix_y)
    

x = np.array([[2,1],[3,7],[5,5],[0,1]])
print(linear_reg(x))