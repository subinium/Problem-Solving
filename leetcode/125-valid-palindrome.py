class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = list(filter(lambda x: x.isalpha() or x.isnumeric(), s.lower()))
        return sp == sp[::-1]
