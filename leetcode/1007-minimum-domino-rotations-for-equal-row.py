class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(n, ts, bs):
            cnt, same, st = 0, 0, ts[0]
            for t, b in zip(ts, bs):
                if t == st:
                    same += t == b
                elif b == st:
                    cnt += 1
                else:
                    return -1
            return min(cnt, n-cnt-same)

        n = len(tops)
        a, b = check(n, tops, bottoms), check(n, bottoms, tops)
        return min(a, b) if not -1 in [a, b] else max(a, b)
