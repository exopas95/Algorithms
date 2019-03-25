# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 02:50:45 2019

@author: Sewoong
"""
import time
start_time = time.time()
count = 0

def swap(a, i, n):
    b = a
    b[i], b[n] = a[n], a[i]
    a = b
    global count
    count += 1
    return a

def permutation(a, n):
    if (n == 1):
        print(a)
        return
    for i in range(n):
        swap(a, i, n - 1)
        permutation(a, n - 1)
        swap(a, i, n - 1)
        
a = [1, 2] 
permutation(a, len(a))
print("swap function used :", count, "times")
time_cost = time.time() - start_time
year = time_cost // (946080000)
month = (time_cost - (year * 946080000)) // 2592000
day = (time_cost - year * (946080000) - month * (2592000)) // (3600 * 24)
hour = (time_cost - year * (946080000) - month * (2592000) - day * (3600 * 24)) // 3600 
minute = (time_cost - year * (946080000) - month * (2592000) - day * (3600 * 24) - hour*3600) // 60
second = time_cost - year * (946080000) - month * (2592000) - day * (3600 * 24) - (hour * 3600) - (minute * 60)
print("Took %s year %s month %s day %s hours %s minutes %s seconds" %(year, month, day, hour, minute, second))
