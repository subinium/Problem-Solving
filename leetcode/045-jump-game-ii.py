class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        st, ed = 0, nums[0]
        cnt = 1
        while ed < n-1:
            cnt += 1
            nxt = max(i + nums[i] for i in range(st, ed+1))
            st, ed = ed, nxt
        return cnt