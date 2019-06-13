# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:53:02 2019

@author: cross
"""

import math 
def interpolationSearch(S,x):
  low = 0
  high= len(S)-1
  location= -1
  if(S[low] <= x and x <= S[high]):
      while (low <= high and location == -1):
          denominator = S[high] - S[low]
          if(denominator == 0):
              mid = low
          else:
              mid = low + math.floor((x - S[low]) * (high - low) / denominator)
          if (x == S[mid]):
              location = mid
          elif(x < S[mid]):
              high = mid - 1
          else:
              low = mid + 1
      return location


S = [1,3,4,7,8,11,13,15,16,20,22,25,29,30,33,36,37,39,41,43,45,48]
x = 11
print(S)
print("Location of %d is %dth" % (x, interpolationSearch(S,x)))
