class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = [], []
        for num in nums:
            if num:
                a.append(num)
            else:
                b.append(num)

        la, lb = len(a), len(b)
        if lb:
            nums[:la], nums[-lb:] = a, b
