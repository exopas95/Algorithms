# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:44:08 2019

@author: cross
"""
import numpy as np

def bin(n, k):
    if(k == 0 or n == k):
        return 1
    else:
        return bin(n - 1, k - 1) + bin(n - 1, k)

def bin2(n, k):
    B = np.zeros((n + 1, k + 1))    
    for i in range (0, n + 1):
        j = 0
        while j <= min(i, k):
            if(j == 0 or j == i):
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j -  1] + B[i - 1][j]
            j += 1
    return B[n][k]

print (bin(10, 5), bin2(10, 5))