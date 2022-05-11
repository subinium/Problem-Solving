class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            s = 0
            for j in range(5):
                s += dp[i-1][j]
                dp[i][j] = s
        return sum(dp[n])