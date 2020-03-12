# import itertools
# import sys

# a, b = map(int, sys.stdin.readline().split())
# List = list(itertools.combinations(range(1, a + 1), b))
# for i in List:
#     print(' '.join(map(str, i)))

import sys
N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1, i+1, N, M)
            visited[i] = False
            out.pop()
solve(0, 0, N, M)
