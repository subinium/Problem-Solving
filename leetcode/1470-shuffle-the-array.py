class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = nums[:]
        new_nums[::2] = nums[:n]
        new_nums[1::2] = nums[n:]
        return new_nums
