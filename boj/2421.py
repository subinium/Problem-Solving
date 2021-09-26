MAX_N = 1000000
era = [1 for _ in range(MAX_N)]

for i in range(2, MAX_N):
    for j in range(i*i, MAX_N, i):
        era[j] = 0

N = int(input())

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + era[int(str(i)+str(j))]

print(dp[N][N]-1)
