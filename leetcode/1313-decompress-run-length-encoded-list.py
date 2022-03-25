class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(0, len(nums), 2):
            ret += [nums[i+1]]*nums[i]
        return ret