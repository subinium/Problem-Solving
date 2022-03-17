class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:], nums2[:] = nums1[:m], nums2[:n]
        p1, p2 = 0, 0
        nums = []
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1

        nums += nums1[p1:m]+nums2[p2:n]
        nums1[:] = nums[:]
