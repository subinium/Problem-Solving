class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ret = []
        for alp in string.ascii_uppercase:
            for i in "123456789":
                if s[0] <= alp <= s[3] and s[1] <= i <= s[4]:
                    ret.append(alp+i)
        return ret
