MOD = 1000000


def f(mode, st, ed):
    if st == ed == 0:
        return 1
    if dp[mode][st][ed] != -1:
        return dp[mode][st][ed]
    dp[mode][st][ed] = 0

    if mode == 0:
        for i in range(st):
            dp[mode][st][ed] += f(1, i, ed+st-i-1)
            dp[mode][st][ed] %= MOD
    else:
        for i in range(ed):
            dp[mode][st][ed] += f(0, st+ed-i-1, i)
            dp[mode][st][ed] %= MOD

    return dp[mode][st][ed]


N = int(input())
dp = [[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(2)]
ans = 0

for i in range(N):
    for j in range(i):
        ans += f(1, j, N-j-2)
    for j in range(i+1, N):
        ans += f(0, j-1, N-j-1)

print(ans % MOD if N > 1 else 1)
