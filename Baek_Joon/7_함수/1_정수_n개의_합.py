"""
[문제: 15596] 
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

[입력]
a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)

[출력]
a에 포함되어 있는 정수 n개의 합 (정수)
"""
import sys


def solve(a):
    ans = sum(a)
    return ans


List = list(map(int, sys.stdin.readline().split()))

print(solve(List))
