"""
백준 알고리즘 1003 
제목: 피보나치 함수
내용: 단순 재귀로 피보나치 수를 구하면 왜 느릴까요? 함수 호출의 개수가 기하급수적으로 늘어나기 때문입니다.
"""
import sys

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