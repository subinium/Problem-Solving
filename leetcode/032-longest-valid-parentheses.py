class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        ck = [0 for _ in range(len(s)+1)]
        for idx, c in enumerate(s):
            if c == '(':
                stk.append(idx)
            elif stk and c == ')':
                top = stk.pop()
                ck[idx] = idx-top+1
                if top:
                    ck[idx] += ck[top-1]
        return max(ck)
