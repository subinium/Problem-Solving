class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums += [2e9]
        ret = []
        st, ed = -2e9, 2e9
        for num in nums:
            if ed+1 != num:
                ret.append(f'{st}->{ed}' if st != ed else str(st))
                st, ed = num, num
            else:
                ed = num
        return ret[1:]
