class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret, total, st = max(nums), 0, 0
        for num in nums:
            while total < 0:
                total -= nums[st]
                st += 1
            total += num
            ret = max(ret, total)
        return ret
