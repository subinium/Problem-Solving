class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            cnt = 0
            for j in range(0, i):
                cnt += dp[j]*dp[i-j-1]
            dp.append(cnt)
        return dp[n]
