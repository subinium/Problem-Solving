class Solution:
    def reverseBits(self, n: int) -> int:
        s = f'{n:032b}'
        return int('0b'+s[::-1], 2)