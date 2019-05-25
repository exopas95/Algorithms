# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:18:40 2019

@author: cross
"""
import utility
import numpy as np

def allShortestPath(g, n):
#node number range(1, n+1)
    d = g
    p = np.zeros((n, n))
    utility.printMatrix(d)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k + 1
    return d, p

def _path(p, q, r):
    if (p[q][r] != 0):
        _path(p, q, p[q][r] - 1)
        print("v%d"%p[q][r], end = " ")
        _path(p, p[q][r] - 1, r)
        
def path(p, q, r):
    print("v%d"% q, end = " ")
    _path(p, q - 1, r - 1)
    print("v%d"% r, end = " ")


inf = 1000
g = [[0, 1, inf, 1, 5],
     [9, 0, 3, 2, inf],
     [inf, inf, 0, 4, inf],
     [inf, inf, 2, 0, 3],
     [3, inf, inf, inf, 0]]

d, p = allShortestPath(g, 5)
print()
utility.printMatrix(d)
print()
utility.printMatrix(p)

path(p, 5, 3)