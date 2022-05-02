class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [even for even in nums if even%2==0] + [odd for odd in nums if odd%2]