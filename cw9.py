# -*- coding: utf-8 -*-
"""
Created on Fri May 13 20:25:05 2022

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
        
def gauss(li):
    size = np.shape(li)[1]
    v = []
    for i in range(size):
        if li[i][i] == 0.0:
            return print('zero')

        for j in range(size):
            if i != j:
                ratio = li[j][i] / li[i][i]
                for k in range(size):
                    li[j][k] = li[j][k] - ratio * li[i][k]
    for i in range(size):
        v.append(li[i][size-1] / li[i][i])
    return v
        
matrix = np.array([[4,-2,4],[3,1,2],[2,4,2]])
print(gauss(matrix))


