class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        S = list(S.lower())
        alp = []
        for idx, c in enumerate(S):
            if c.isalpha():
                alp.append(idx)

        def convert(s, x):
            ss = s[:]
            for i in range(len(alp)):
                if ((1 << i) & x) > 0:
                    ss[alp[i]] = s[alp[i]].upper()

            return ''.join(ss)

        return [convert(S, i) for i in range(2**len(alp))]
