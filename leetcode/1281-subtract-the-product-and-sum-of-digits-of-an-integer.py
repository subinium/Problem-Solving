class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = sum([int(i) for i in str(n)])
        p = 1
        while n:
            n, p = n//10, p*(n % 10)
        return p-s
