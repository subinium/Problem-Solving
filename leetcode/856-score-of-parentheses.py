class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ret = 0
        sub, cnt = "", 0
        for c in s:
            cnt += 1 if c == '(' else -1
            sub += c
            if cnt == 0:
                ret += 1 if sub == '()' else 2 * \
                    self.scoreOfParentheses(sub[1:-1])
                sub = ""
        return ret
