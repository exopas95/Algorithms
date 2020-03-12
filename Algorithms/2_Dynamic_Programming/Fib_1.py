"""
백준 알고리즘 2748 
제목: 피보나치 수 2
내용: 동적 계획법으로 피보나치 수를 계산하는 문제
"""
import sys

# def Fib(length):
#     if length == 0:
#         return 0
#     elif length == 1:
#         return 1
#     else:
#         answer = Fib(length - 1) + Fib(length - 2)
#         return answer

def Fib(index):
    for i in range(2, index + 1):
        answer[i] = answer[i - 1] + answer[i - 2]
    print(answer[-1])

N = int(sys.stdin.readline())
answer = []
for i in range(0, N + 1):
    answer.append(0)
answer[1] = 1
Fib(N)