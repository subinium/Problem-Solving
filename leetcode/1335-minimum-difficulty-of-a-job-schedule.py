class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        jl = len(jobs)
        if jl < d:
            return -1

        dp = [[0 for i in range(jl)] for j in range(jl)]
        dp2 = [[2e9 for i in range(jl)] for j in range(d)]
        for i in range(jl):
            dp[i][i] = jobs[i]
            for j in range(i+1, jl):
                dp[i][j] = max(dp[i][j-1], jobs[j])

        dp2[0][0] = jobs[0]
        for i in range(1, jl):
            dp2[0][i] = max(dp2[0][i-1], jobs[i])

        for i in range(1, d):
            for j in range(i, jl):
                for k in range(j, jl):
                    dp2[i][k] = min(dp2[i][k], dp2[i-1][j-1]+dp[j][k])

        return dp2[d-1][jl-1]
