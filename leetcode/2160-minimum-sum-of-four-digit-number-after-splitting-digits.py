class Solution:
    def minimumSum(self, num: int) -> int:
        s=''.join(sorted(str(num)))
        return int(s[::2])+int(s[1::2])