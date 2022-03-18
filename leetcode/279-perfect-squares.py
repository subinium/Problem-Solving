class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = dp[i-1]+1
            p = 2
            while p*p <= i:
                dp[i] = min(dp[i], dp[i-p*p]+1)
                p += 1

        return dp[n]
