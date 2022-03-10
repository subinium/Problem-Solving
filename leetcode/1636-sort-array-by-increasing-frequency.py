class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        arr = sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0]))
        ret = []
        for num, cnt in arr:
            ret += [num]*cnt
        return ret
