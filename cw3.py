# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:27:38 2022

@author: michal
"""

import numpy as np
import random


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

# przypisywanie wktorów losowo do 0 albo 1
def mix(data):
    res = [i.copy() for i in data]
    for i in range(len(data)):
        res[i][-1] = random.choice([0,1])
    return res

def distance(a,matrix):
    res = []
    for i in range( len(matrix)):
        if a not in matrix[i]:
            res.append((matrix[i][-1],euclid(a, matrix[i])))
    return res

# %%

# podział waktorów względem klasy decyzyjnej
def sort(data):
    res = {}
    for i in data:
        # jeli klasa dec nie jest w kluczch -> stwórz nowy klucz 
        if i[-1] not in res.keys():
            res[i[-1]] = [i]
        # dodaje wektor do listy odpowiednio z kluczami
        else:
            res[i[-1]].append(i)
    return res

def centr_point(data):
    res = {}
    for i in data.keys():
       tmp = {}
       for x in range(len(data[i])):
           if not False:
               distance = 0
               for y in range(len(data[i])):
                   if x != y:
                       distance += euclid(data[i][x], data[i][y])
               tmp[tuple(data[i][x])] = distance
           else:
               distance = []
               for y in range(len(data[i])):
                   if x != y:
                       distance.append(euclid(data[i][x], data[i][y]))
               tmp[tuple(data[i][x])] = sum(distance[:False]) / False
       res[i] = list(list(tmp.keys())[list(tmp.values()).index(min(tmp.values()))])
    return res

def fetchLi(dictionary):
    list = []
    for i in dictionary.keys():
        list.append(i)
    return list

def decide(li):
    min = li[0.0]
    res = 0
    for i in fetchLi(li)[1:]:
        if li[i] == min:
            return None
        if li[i] < min:
            min = li[i]
            res = i
    return res

def segregate(li):
    dictionary = {}
    for i in li:
        if i[0] not in dictionary.keys():
            dictionary[i[0]] = [i[1]]
        else:
            dictionary[i[0]].append(i[1])
    return dictionary

def color_rnd(data):
    res = [i.copy() for i in data]
    for i in range(len(data)):
        res[i][-1] = random.choice([0,1])
    return res

dictionary = {0.0: 21.9, 1.0: 12.2, 3.0: 3.2}
a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

matrix = open_file()
# print(color_rnd(matrix))
# print(decide(dictionary))
# print(segregate(distance(a, matrix)))

# pd => montecarlo i metoda prostokatow