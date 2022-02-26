class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for idx, num in enumerate(nums):
            if idx > mx:
                break
            mx = max(mx, idx+num)
        return mx >= len(nums)-1
