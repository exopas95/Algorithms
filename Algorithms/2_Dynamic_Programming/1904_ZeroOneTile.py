"""
백준 알고리즘 1904 
제목: 01 타일
내용: 점화식의 값을 특정 상수로 나눈 나머지를 구하는 문제
"""

import sys
import itertools

N = int(sys.stdin.readline())
a = 1
b = 2
temp = 0

for i in range(0, N - 2):
    temp = a + b
    a = b
    b = temp
print(b % 15746)