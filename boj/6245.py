N = int(input())
card2num = {str(i): i for i in range(2, 10)}
card2num.update({'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13})

lst = [[0]+[card2num[c[0]] for c in input().split()]
       for _ in range(N)] + [[0 for _ in range(N+1)]]
lst.reverse()

for i in range(1, N+1):
    for j in range(1, N+1):
        lst[i][j] += max(lst[i-1][j], lst[i][j-1])

print(lst[N][N])
