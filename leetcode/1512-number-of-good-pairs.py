class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ret = 0
        for key, val in cnt.items():
            ret += val*(val-1)//2
        return ret
