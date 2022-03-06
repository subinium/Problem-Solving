class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dct = {new: orig for new, orig in zip(order, string.ascii_lowercase)}
        for idx, word in enumerate(words):
            new_word = ''.join([dct[c] for c in word])
            words[idx] = new_word
        return sorted(words) == words
