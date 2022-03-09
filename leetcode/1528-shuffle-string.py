class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([c for _, c in sorted(zip(indices, s))])
