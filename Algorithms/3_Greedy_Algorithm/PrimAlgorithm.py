# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:30:35 2019

@author: cross
"""

import utility

inf = 1000
w = [[0,  1,  3,inf, inf],
    [1,  0,  3,6,   inf],
    [3,  3,  0,4,   2],
    [inf,6,  4,0,   5],
    [inf,inf,2,5,   0]]

F = set()
utility.printMatrix(w)
n = len(w)
nearest = n * [0]
distance = n * [0]

for i in range(1, n):
    nearest[i] = 0
    distance[i] = w[0][i]

#Prim Algorithm
for index in range(1, n):
    min = inf
    for i in range(1, n):
        if(0 <= distance[i] and distance[i] < min):
            min = distance[i]
            vnear = i

    F.add((vnear, nearest[vnear]))
    
    distance[vnear] = -1
    
    for i in range(1, n):
        if(w[i][vnear] < distance[i]):
            distance[i] = w[i][vnear]
            nearest[i] = vnear

print()
print(F)