class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(str(dividend/divisor).split('.')[0])
        return max(min(result, int(2**31-1)), int(-2**31))
