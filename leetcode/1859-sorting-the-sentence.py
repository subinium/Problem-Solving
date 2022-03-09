class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(map(lambda x: x[:-1], sorted(s.split(), key=lambda x: x[-1])))
