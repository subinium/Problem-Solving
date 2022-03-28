class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        s = sorted(nums)
        return nums==s or nums==s[::-1]