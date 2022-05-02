class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def new_string(s):
            stk = []
            for c in s:
                if c=='#': 
                    if stk: stk.pop()
                else: stk.append(c)
            return stk
        return new_string(s)==new_string(t)