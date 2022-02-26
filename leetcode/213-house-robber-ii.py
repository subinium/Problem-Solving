class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1 = [0]+nums[1:]
        nums2 = [0]+nums[:-1]
        for i in range(3, len(nums1)):
            nums1[i] += max(nums1[i-2], nums1[i-3])
        for i in range(3, len(nums2)):
            nums2[i] += max(nums2[i-2], nums2[i-3])
        return max(nums1+nums2)
