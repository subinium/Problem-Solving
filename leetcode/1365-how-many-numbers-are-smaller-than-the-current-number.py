class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum([num2 < num for num2 in nums]) for num in nums]
