class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dct = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in '({[':
                stk.append(c)
            elif len(stk) == 0:
                return False
            elif dct[c] == stk[-1]:
                stk.pop()
            else:
                return False
        return len(stk) == 0
