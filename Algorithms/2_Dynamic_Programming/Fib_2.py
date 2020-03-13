"""
백준 알고리즘 1003 
제목: 피보나치 함수
내용: 단순 재귀로 피보나치 수를 구하면 왜 느릴까요? 함수 호출의 개수가 기하급수적으로 늘어나기 때문입니다.
"""
import sys

def Fib(index):
    for i in range(2, index + 1):
        answer[i] = [answer[i - 1][0] + answer[i - 2][0], answer[i - 1][1] + answer[i - 2][1]]
    result = str(answer[-1][0]) + " " + str(answer[-1][1])
    return result

N = int(sys.stdin.readline())
a_List = []

for i in range(0, N):
    n_input = int(sys.stdin.readline())
    if n_input == 0:
        a_List.append("1 0")
    elif n_input == 1:
        a_List.append("0 1")
    else:
        answer = [[0, 0]] * (n_input + 1)
        answer[0] = [1, 0]
        answer[1] = [0, 1]
        a_List.append(Fib(n_input))

for anw in a_List:
    print(anw)