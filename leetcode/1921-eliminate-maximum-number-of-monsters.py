class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([d/s for d, s in zip(dist, speed)])
        for idx, t in enumerate(time):
            if idx >= t:
                return idx
        return len(time)
