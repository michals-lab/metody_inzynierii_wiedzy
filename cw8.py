# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:32:57 2022

@author: michal
"""
import numpy as np

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

def ak(matrix, k):
    for x in range(len(matrix)):
        if (matrix == np.transpose(matrix)).all():
            for x in range(k):
                q, r = q_r(matrix)
                matrix = np.dot(r,q)
            return matrix
        else:
            return

def triang_matrix(matrix, sigma = 0.001):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y < x:
                if matrix[x][y] > sigma:
                    return False
    return True


def eig_values(matrix):
    for x in range(len(matrix)):
        if (matrix == np.transpose(matrix)).all():
            while not triang_matrix(matrix):
                q, r = q_r(matrix)
                matrix = np.dot(r,q)
            return matrix
        else:
            return
        
a=np.array([[1.,2.,3.,4.,5.],[2.,2.,3.,4.,5.],[3.,3.,3.,4.,5.],[4.,4.,4.,4.,5.],[5.,5.,5.,5.,5.]])
print(eig_values(a))