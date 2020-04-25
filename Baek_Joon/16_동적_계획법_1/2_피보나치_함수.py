"""
[문제: 1003] 
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

[출력]
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
"""
import sys


def Fib(index):
    for i in range(2, index + 1):
        answer[i] = [answer[i - 1][0] + answer[i - 2]
                     [0], answer[i - 1][1] + answer[i - 2][1]]
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
