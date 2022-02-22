from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        p = defaultdict(lambda: -1e10)
        for idx, num in enumerate(nums):
            if idx-p[num] <= k:
                return True
            p[num] = idx
        return False
