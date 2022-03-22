class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z, alp = divmod(k-n-1, 25)
        return (n-z-1)*'a'+chr(ord('a')+alp+1)+z*'z'
