class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = set()
        lst = 0
        answer = 0
        for idx, c in enumerate(s):
            while c in alpha:
                alpha.remove(s[lst])
                lst += 1
            alpha.add(c)
            answer = max(answer, len(alpha))
        return answer
