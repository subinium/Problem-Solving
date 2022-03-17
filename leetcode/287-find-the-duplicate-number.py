class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        ck = [0 for _ in range(n)]
        for num in nums:
            if ck[num]:
                return num
            ck[num] += 1
