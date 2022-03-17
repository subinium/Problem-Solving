class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnts = [0, 0, 0]
        for i in nums:
            cnts[i] += 1
        cnt, c = 0, 0
        for i in range(len(nums)):
            while cnt == cnts[c]:
                cnt, c = 0, c+1
            nums[i] = c
            cnt += 1
