class Solution:
    def replaceDigits(self, s: str) -> str:
        ret = ''
        n = len(s)
        for i in range(0, n, 2):
            ret += s[i]
            if i+1<n: ret += chr(ord(s[i])+int(s[i+1]))
        return ret