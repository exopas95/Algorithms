# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:54:35 2019

@author: cross
"""

import utility
a=['A','A','C','A','G','T','T','A','C','C']
b=['T','A','A','G','G','T','C','A']

m=len(a)
n=len(b)
table=[[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[ (0,0) for j in range(0,n+1)] for i in range(0,m+1)]

for j in range(n-1,-1,-1):
    table[m][j] =table[m][j+1]+2

for i in range(m-1,-1,-1):
    table[i][n] =table[i+1][n]+2

for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        penalty = 0
        if a[i] != b[j]:
            penalty = 1
        tmin = table[i+1][j+1] + penalty
        minindex[i][j] = (i+1, j+1)
        if tmin > table[i+1][j] + 2:
            tmin = table[i+1][j] + 2
            minindex[i][j] = (i+1, j)
        if tmin > table[i][j+1] + 2:
            tmin = table[i][j+1] + 2
            minindex[i][j] = (i, j+1)
        table[i][j] = tmin


utility.printMatrix(table)
x=0
y=0

while (x <m and y <n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)= minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ",  b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")
