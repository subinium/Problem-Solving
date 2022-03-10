class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        lst = []
        for num, idx in zip(nums, index):
            lst.insert(idx, num)
        return lst
