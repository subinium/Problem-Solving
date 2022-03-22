class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = -1
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                p1 = i

        p2 = p1+1
        for i in range(p1, n):
            if nums[p1] < nums[i] <= nums[p2]:
                p2 = i

        if p1 >= 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
        nums[p1+1:] = reversed(nums[p1+1:])
