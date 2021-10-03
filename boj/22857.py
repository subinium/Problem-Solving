N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    arr[i] %= 2
    for j in range(0, K+1):
        if j and arr[i]:
            dp[i][j] = dp[i-1][j-1]
        if arr[i] == 0:
            dp[i][j] = dp[i-1][j]+1

print(max([max(i) for i in dp]))
