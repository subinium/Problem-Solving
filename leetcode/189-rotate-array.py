class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if n == 1 or k == 0:
            return
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
