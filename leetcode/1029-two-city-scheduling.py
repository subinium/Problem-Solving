# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         n = len(costs)//2
#         dp = [[1e9 for _ in range(n+1)] for _ in range(n+1)]
#         dp[0][0] = 0
#         for idx, (ac, bc) in enumerate(costs, 1):
#             for i in range(idx+1):
#                 j = idx-i
#                 if i>n or j>n: continue
#                 tmp = [dp[i][j]]
#                 if i: tmp += [dp[i-1][j]+ac]
#                 if j: tmp += [dp[i][j-1]+bc]
#                 dp[i][j]=min(tmp)
#         return dp[n][n]
    
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n, costs = len(costs), sorted(costs, key=lambda x:x[1]-x[0])
        return sum([c[i<n//2] for i, c in enumerate(costs)])    