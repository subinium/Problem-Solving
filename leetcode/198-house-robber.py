class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0]+nums
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums)
