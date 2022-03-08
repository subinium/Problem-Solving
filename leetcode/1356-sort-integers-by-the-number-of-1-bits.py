class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countOne(n):
            return str(bin(n)).count('1')
        return [j for _, j in sorted([(countOne(i), i) for i in arr])]
