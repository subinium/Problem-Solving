from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dp = [[-1 for _ in range(1 << n)] for _ in range(n)]
        q = deque()
        for i in range(n):
            q.append((i, 1 << i))
            dp[i][1 << i] = 0

        while q:
            now, state = q.popleft()
            if state == (1 << n)-1:
                return dp[now][state]

            for nxt in graph[now]:
                state_tmp = state | (1 << nxt)
                if dp[nxt][state_tmp] == -1:
                    q.append((nxt, state_tmp))
                    dp[nxt][state_tmp] = dp[now][state]+1
