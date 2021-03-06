# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:24:09 2019

@author: cross
"""

def kp_BFS():
        global maxProfit
        global bestset
        
        q = queue.Queue()
        root = Node(-1, 0, 0, [])
        q.put(root)
        bound = 0
        while not q.empty():
            v = q.get()
            uLevel = v.level + 1
            v.include.append(1)
            t = v.include[:]
            u = Node(uLevel, v[uLevel], v.profit+p[uLevel], t)
            bound = compBound(u)
            if u.weight <= W and u.profit > maxProfit:
                maxProfit = u.profit
                bestset = u.include[:]
            if bound > maxProfit:
                q.put(u)
            v.include.pop()
            v.incloude.append(0)
            t = v.include[:]
            u = Node(uLevel, v.weight, v.profit, t)
            bound = compBound(u)
            include[uLevel] = 0
            if bound > maxProfit:
                q.put(u)


def compBound(u):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while(j <= n-1 and totweight + w[j] <= W):
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if (k <= n-1 ):
            result += (W - totweight) * p[k] / w[k]
        return result

        
n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
include=[0]*n
maxProfit =0
bestset=n*[0]
kp_BFS()
print(bestset)
