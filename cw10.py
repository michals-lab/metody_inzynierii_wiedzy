# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:47:22 2022

@author: michal
"""

import numpy as np
import math


x = [1,1,1,1,1,1,1,1]
y = [1,1,1,1,-1,-1,-1,-1]
z = [1,1,-1,-1,0,0,0,0]
a = [0,0,0,0,1,1,-1,-1]
b = [1,-1,0,0,0,0,0,0]
c = [0,0,1,-1,0,0,0,0]
d = [0,0,0,0,1,-1,0,0]
e = [0,0,0,0,0,0,1,-1] 

matrix = np.array([x,y,z,a,b,c,d,e])

q = np.array([8,6,2,3,4,6,6,5])

# znoramilzować wektory następnie dzielimy wszystkie elementy i wyiwetlamy

def dot_prod(v1,v2):
    v3=0
    for i in range(len(v1)):
        v3 += v1[i]*v2[i]
    return v3

def len_v(v):
    return math.sqrt(dot_prod(v,v))


baza = np.dot(matrix, matrix.T) # AA^T

print("baza\n",baza)
print(np.diag(baza))


orthogonal = []
tmp = 0
for row in matrix:
    tmp=0
    for i in row:
        tmp+=abs(i) # wartoć bezwzględna
    orthogonal.append(tmp)

print("orthogonal\n",orthogonal)
print("orthogonal dot_prod\n",dot_prod(baza[0],baza[3]))

orthonormal = []

for i in range(len(matrix[4])):
    tmp = matrix[i]*(1/math.sqrt(orthogonal[i]))
    orthonormal.append(tmp)
    
orthonormal = np.array(orthonormal)
print("orthonormal\n",orthonormal)

print("test\n",dot_prod(orthonormal,orthonormal))

print("ortnorm\n",orthonormal.T)
print("odwrotnosc\n",np.linalg.inv(orthonormal)) #jest wbudowana do numpy funkcja odwracająca 
print("AA^-1\n",np.dot(orthonormal,np.linalg.inv(orthonormal))) # AA^-1

#zamiana baz

zamiana = np.dot(orthonormal,q)
print(zamiana)


#print(dot_prod(x, y))
#print('np.dot =>',np.dot(matrix,matrix))
#print(np.transpose(matrix))