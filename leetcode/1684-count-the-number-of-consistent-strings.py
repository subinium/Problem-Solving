class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        key = set(allowed)
        return sum([len(set(word)-key) == 0 for word in words])
