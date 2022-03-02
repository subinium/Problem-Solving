class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx, ls = 0, len(s)
        t += ' '
        for c in t:
            if idx == ls:
                return True
            if s[idx] == c:
                idx += 1
        return False
