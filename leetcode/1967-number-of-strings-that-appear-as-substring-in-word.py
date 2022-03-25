class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(map(lambda x:x in word, patterns))