class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ret = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                ret *= -1
        return ret
