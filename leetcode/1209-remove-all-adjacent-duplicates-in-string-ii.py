class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk and stk[-1][0]==c: stk.append((c, stk[-1][1]+1))
            else: stk.append((c, 1))
            if stk[-1][1]==k:
                stk = stk[:-k]
        return ''.join([x[0] for x in stk])