class Solution:
    def freqAlphabets(self, s: str) -> str:
        lc = string.ascii_lowercase
        dct = [(str(i+1)+'#', lc[i]) for i in range(9, 26)] + \
            [(str(i+1), lc[i]) for i in range(9)]
        for k, v in dct:
            s = s.replace(k, v)
        return s
