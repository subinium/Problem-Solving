N, M = map(int, input().split())
m, w = [[0]+sorted(list(map(int, input().split()))) for _ in range(2)]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j-1] + abs(m[i] - w[j])
        dp[i][j] = min(dp[i][j], dp[i - (i > j)][j - (i < j)])


print(dp[N][M])
