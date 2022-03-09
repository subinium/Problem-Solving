class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret = [first]
        for i in encoded:
            ret.append(ret[-1] ^ i)
        return ret
