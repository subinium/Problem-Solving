class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([key for key, val in Counter(nums).items() if val == 1])
