"""
백준 알고리즘 11053 
제목: 가장 긴 증가하는 부분 수열
내용: LIS(Longest Increasing Subsequence)를 구하는 문제
"""
import sys

N = int(sys.stdin.readline())
List = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    dp[i] = 1                                           # 자기 자신을 선택했을 때 수열의 길이는 1
    for j in range(0, i):                               # 자기 자신과 자기 이전의 값을 비교하는 비교문
        if List[i] > List[j] and dp[j] + 1 > dp[i]:     # 작은 값일 때 && 자기보다 작은 길이의 부분순열일 때
            dp[i] = dp[j] + 1                           # 이전 부분 순열 조합에 자신을 더한 값

print(max(dp))