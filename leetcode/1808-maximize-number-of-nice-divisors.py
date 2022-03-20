class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = int(1e9+7)
        three, r = divmod(primeFactors, 3)
        if three and r == 1:
            three, r = three-1, 4
        if r == 0:
            r = 1
        return pow(3, three, MOD)*r % MOD
