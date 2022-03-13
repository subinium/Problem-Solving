class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums = [-10005]+nums+[10005]
        st, ed = 0, len(nums)
        while st < ed:
            mid = (st+ed+1)//2
            if target <= nums[mid]:
                ed = mid-1
            else:
                st = mid

        return st
