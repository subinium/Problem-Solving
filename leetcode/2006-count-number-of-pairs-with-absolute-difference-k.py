class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                cnt += abs(nums[i]-nums[j]) == k

        return cnt
