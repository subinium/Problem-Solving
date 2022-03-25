class Solution:
    def maximum69Number (self, num: int) -> int:
        s=list(str(num))
        if '6' in s:
            s[s.index('6')]='9'
        return int(''.join(s))