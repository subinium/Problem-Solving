class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = None
        p = 0
        for i in range(n):
            if nums[i] != None:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        return p
