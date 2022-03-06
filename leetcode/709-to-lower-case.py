class Solution:
    def countOrders(self, n: int) -> int:
        ret = 1
        for i in range(1, n+1):
            i *= 2
            ret = ret*i*(i-1)//2 % int(1e9+7)
        return ret
