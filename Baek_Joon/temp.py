# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

N, K = map(int, sys.stdin.readline().split())
List = list(map(int, sys.stdin.readline().split()))
count = 0
condition = True

while len(List) >= K:
    temp_list = List[0:K]
    min_num = min(temp_list)

    for i in range(0, len(temp_list) - 1):
        if temp_list[i] == temp_list[i + 1] and temp_list[i] == min_num:
            condition = False
        else:
            condition = True

    if condition == True:
        for i in range(0, K):
            List[i] = min_num
        count += 1
    List.pop(List[0])


print(count)
