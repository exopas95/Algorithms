# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:29:54 2019

@author: cross
"""


import numpy as np

def strassen (n, A, B, C):
    if (n <= 2):
        C = np.dot(A, B)
    else:
        for i in range(1, n)
        

n = 32
A = np.ones(shape = (n, n)) + 4
B = np.ones(shape = (n, n)) + 6
C = np.dot(A, B)
print(C)

result = strassen(n, A, B, C)
print(result)
