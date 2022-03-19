class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        s, e = -1, -1
        for st, ed in intervals:
            if st <= e:
                e = max(e, ed)
            else:
                ret.append([s, e])
                s, e = st, ed
        ret.append([s, e])
        return ret[1:]
