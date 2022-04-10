class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stk = []
        for i in ops:
            if i=='+': stk.append(sum(stk[-2:]))
            elif i=='D': stk.append(stk[-1]*2)
            elif i=='C': stk.pop()
            else: stk.append(int(i))
        return sum(stk)
            