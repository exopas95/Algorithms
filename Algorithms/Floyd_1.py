# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:18:32 2019

@author: cross
"""
import numpy as np

def allShortestPath(g, n):
#node number range(1, n+1)
    d = g
    p = np.zeros((n, n))
    printMatrix(d)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k + 1
    return d, p
    
def printMatrix(d):
    n = len(d[0])
    for i in range(0, n):
        for j in range(0, n):
            print(d[i][j], end = " ")
        print()

inf = 1000
g = [[0, 1, inf, 1, 5],
     [9, 0, 3, 2, inf],
     [inf, inf, 0, 4, inf],
     [inf, inf, 2, 0, 3],
     [3, inf, inf, inf, 0]]

d, p = allShortestPath(g, 5)
print()
printMatrix(d)
print()
printMatrix(p)