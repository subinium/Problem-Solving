class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk, fix = [], [0 for _ in range(len(s))]
        for idx, c in enumerate(s):
            if c == '(':
                stk.append(idx)
            elif c == ')':
                if len(stk):
                    fix[stk.pop()] = fix[idx] = True
            else:
                fix[idx] = True

        ret = ""
        for c, f in zip(s, fix):
            ret += c*f
        return ret
