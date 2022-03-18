class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stk = []
        answer = 0
        for p in prices:
            while stk and stk[-1] > p:
                stk.pop()
            stk.append(p)
            answer = max(answer, stk[-1]-stk[0])
        return answer
