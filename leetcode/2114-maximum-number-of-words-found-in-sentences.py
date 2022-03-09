class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(map(lambda x: len(x.split()), sentences))
