# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:08:41 2019

@author: cross
"""

def quickSort (s, low, high):
    pivotpoint = -1
    if (high > low):
        pivotpoint = partition(s, low, high)
        quickSort(s, low, pivotpoint - 1)
        quickSort(s, pivotpoint + 1, high)

def partition (s, low, high):
    pivotItem = s[low]
    j = low
    for i in range(low + 1, high + 1):
        if(s[i] < pivotItem):
            j += 1
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
    pivotpoint = j
    temp = s[low]
    s[low] = s[pivotpoint]
    s[pivotpoint] = temp
    return pivotpoint
    

s = [3, 5, 2, 9, 10, 14, 4, 8]
quickSort (s, 0, 7)
print(s)