class Solution:
    def isHappy(self, n: int) -> bool:
        ck = [False for _ in range(1000)]

        def nxt(n):
            return sum(int(i)**2 for i in str(n))
        n = nxt(n)
        while not ck[n]:
            ck[n] = True
            n = nxt(n)

        return n == 1
