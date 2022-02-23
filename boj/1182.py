import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    cnt += sum([sum(c) == M for c in combinations(arr, i)])

print(cnt)
