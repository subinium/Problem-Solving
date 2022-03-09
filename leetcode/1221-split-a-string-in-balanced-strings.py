class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ret, val = 0, 0
        for c in s:
            val += 1 if c == 'L' else -1
            ret += val == 0
        return ret
