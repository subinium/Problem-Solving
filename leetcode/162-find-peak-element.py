class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums += [-4e9]
        for i in range(len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
