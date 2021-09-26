dp = [[0, 0] for _ in range(50)]
dp[0][0] = 1

for i in range(1, 50):
    dp[i][0], dp[i][1] = dp[i-1][0] + dp[i-1][1], dp[i-1][0]

for i in range(1, int(input())+1):
    print(f'Scenario #{i}:')
    print(sum(dp[int(input())]))
    print()
