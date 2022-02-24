class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        st, ed = 0, l-1
        while st < ed:
            mid = (st+ed+1)//2
            if nums[mid] <= target:
                st, ed = mid, ed
            else:
                st, ed = st, mid-1

        return st if nums[st] == target else -1
