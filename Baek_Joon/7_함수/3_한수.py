"""
[문제: 1546] 
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

[입력]
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

[출력]
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""
import sys


def one_number(n):
    count = 99
    for i in range(100, n + 1):
        List = list(map(int, list(str(i))))
        if List[1] - List[0] == List[2] - List[1]:
            count += 1
    return count


N = int(sys.stdin.readline())
if N < 100:
    print(N)
else:
    print(one_number(N))
