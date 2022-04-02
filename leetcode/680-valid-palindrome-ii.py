class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s):
            return s==s[::-1]
        
        n = len(s)
        st, ed = 0, n-1
        while st < ed:
            if s[st]==s[ed]: st, ed = st+1, ed-1
            else: return palindrome(s[st:ed]) or palindrome(s[st+1:ed+1])
        return True