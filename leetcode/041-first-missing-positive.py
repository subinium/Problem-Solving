class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] = 1
        n = 1
        while d[n]:
            n += 1
        return n
