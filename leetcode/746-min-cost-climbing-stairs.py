class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            cost[i] = cost[i]+min(cost[i-1], cost[i-2])
        return min(cost[-2:])
