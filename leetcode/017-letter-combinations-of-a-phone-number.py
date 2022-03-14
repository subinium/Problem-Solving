class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alps = "//abc/def/ghi/jkl/mno/pqrs/tuv/wxyz".split('/')
        return [''.join(x) for x in product(*map(lambda x: alps[int(x)], digits))] if digits else []
