class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(answer, lst, idx, dp, s, l):
            if idx == l:
                answer.append(lst[:])
                return
            for i in range(idx, l):
                if dp[idx][i]:
                    lst.append(s[idx:i+1])
                    dfs(answer, lst, i+1, dp, s, l)
                    lst.pop()

        answer = []
        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = True
            if i != N-1:
                dp[i][i+1] = s[i] == s[i+1]

        for j in range(2, N):
            for i in range(N):
                if i+j >= N:
                    break
                dp[i][i+j] = s[i] == s[i+j] and dp[i+1][i+j-1]

        dfs(answer, [], 0, dp, s, N)
        return answer
