class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s)+[' '], sorted(t)
        for i, j in zip(s, t):
            if i != j:
                return j
