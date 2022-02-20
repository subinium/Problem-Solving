# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        st, ed = 1, n
        while st < ed:
            mid = (st+ed)//2
            if isBadVersion(mid):
                st, ed = st, mid
            else:
                st, ed = mid+1, ed
        return st
