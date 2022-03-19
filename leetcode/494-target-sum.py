class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        now = defaultdict(lambda: 0)
        now[0] = 1
        for num in nums:
            nxt = defaultdict(lambda: 0)
            for k, v in now.items():
                nxt[k-num] += v
                nxt[k+num] += v
            now = nxt
        return now[target]
