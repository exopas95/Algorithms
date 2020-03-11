import itertools
import sys

a, b = map(int, sys.stdin.readline().split())
P = itertools.permutations(range(1, a + 1), b)
for i in P:
    print(' '.join(map(str, i)))
