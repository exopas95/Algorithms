# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:53:21 2019

@author: cross
"""

def promising(i,weight, total):
    if((weight + total >= W) and (weight == W or weight + w[i+1] <= W)):
        return True;

def s_s(i, weight, total, include):
    if(promising(i, weight, total) == True):
        if(weight == W):
            print("sol", include)
        else:
            include[i + 1] = 1
            s_s(i + 1, weight + w[i + 1], total - w[i + 1], include)
            include[i + 1] = 0
            s_s(i+1, weight, total - w[i+1], include)


n=4
w=[1,4,2,6]

W=6
print("items =",w, "W =", W)
include = n*[0]
total=0
for k in w:
    total+=k
#인덱스 -1로 넘겨주는거 유의
s_s(-1,0,total,include)
