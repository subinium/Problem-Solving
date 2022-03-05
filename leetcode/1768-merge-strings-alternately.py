class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        lm = min(l1, l2)
        ret = ''
        for i in range(lm):
            ret += word1[i]+word2[i]
        return ret + word1[lm:]+word2[lm:]
