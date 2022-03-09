class Solution:
    def maxDepth(self, s: str) -> int:
        ret, val = 0, 0
        for c in s:
            if c == '(':
                val += 1
            elif c == ')':
                val -= 1
            ret = max(ret, val)
        return ret
