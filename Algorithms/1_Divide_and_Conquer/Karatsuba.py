# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:18:13 2019

@author: cross
"""
import time

def prod2(a, b):
    threshold = 4
    n1 = len(str(a))
    n2 = len(str(b))
    
    if (n1 > n2):
        n = n1
    else:
        n = n2
    
    if (a == 0 or b == 0):
        return 0
    elif n < threshold:
        return a * b
    else:
        m = int(n / 2)
        x = int(a / (10 ** m))
        y = a % (10 ** m)
        w = int(b / (10 ** m))
        z = b % (10 ** m)
        print(x, y, w, z)
        
        r = prod2(x + y, w + z)
        p = prod2(x, w)
        q = prod2(y, z)
        
        return p * (10 ** (2 * m)) + (r - p - q) * (10 ** m) + q
    return 0

a = 12345678
b = 23456789

s1 = time.time()
result1 = prod2(a, b)
e1 = time. time()
print(result1, "Took %s seconds" %(e1 - s1))

s2 = time.time()
result2 = a * b
e2 = time.time()
print(result2, "Took %s seconds" %(e2 - s2))