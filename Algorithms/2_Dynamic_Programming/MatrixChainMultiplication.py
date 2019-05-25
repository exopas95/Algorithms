# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:54:02 2019

@author: cross
"""

import utility

def order(p, i, j):
    if(i == j):
        print("A", i, end="")
    else:
        k = p[i][j]
        print("(", end="")
        order(p, i, k)
        order(p, k+1, j)
        print(")", end="")
    
d=[5,2,3,4,6,7,8]
n=len(d)-1

m=[[0 for j in range(1,n+2)] for i in range(1,n+2)]
p=[[0 for j in range(1,n+2)] for i in range(1,n+2)]

for dia in range(1, n):
    for i in range(1, n - dia + 1):
        j = i + dia
        small = 1000
        for k in range(i, j):
            t = m[i][k] + m[k+1][j] + d[i-1] * d[k] * d[j]
            if(t < small):
                small = t
                m[i][j] = t
                p[i][j] = k

utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p,1,6)
