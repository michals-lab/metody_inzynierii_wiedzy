# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:28:33 2022

@author: michal
"""

import numpy as np

matrix = []

def open_file():
    with open("australian.dat","r") as file:
        matrix = [list(map(lambda a: float(a),line.split())) for line in file]
        return matrix

# open_file()    

def euclid(lst1, lst2):
    tmp = 0
    for i in range(max(len(lst1),len(lst2))-1):
        tmp += pow((lst1[i] - lst2[i]),2)
    res = np.sqrt(tmp)
    return res

matrix = open_file()
# print(euclid(matrix[0],matrix[1]))
# print(euclid(matrix[21],matrix[37]))

# pd => odlelosc kazdego od zera, grupowanie wg klasy decyzyjnej
# %%
def distance(a,matrix):
    res = []
    for i in range( len(matrix)):
        if a not in matrix[i]:
            res.append((matrix[i][-1],euclid(a, matrix[i])))
    return res

def k_nearest_neighbors(dictionary, x):
    for i in dictionary.keys():
        dictionary[i].sort()
        dictionary[i] = sum(dictionary[i][:x])
    return dictionary

def group(li):
    res = {}
    for i in li:
        if i[0] not in res.keys():
            res[i[0]] = [i[1]]
        else:
            res[i[0]].append(i[1])
    return res

a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print(distance(a, matrix))
# print(k_nearest_neighbors(group(distance(a,matrix)), 5))
        

