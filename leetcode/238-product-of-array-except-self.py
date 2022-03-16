class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0) > 1
        product, product2 = 1, 1
        for i in nums:
            product *= i
            if i:
                product2 *= i
        return [product//num if num else (0 if zeros else product2) for num in nums]
