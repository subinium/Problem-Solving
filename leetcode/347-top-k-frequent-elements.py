class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = list(Counter(nums).items())
        cnts.sort(key=lambda x: x[1], reverse=True)
        return [num for num, _ in cnts[:k]]

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         return [n for n, _ in sorted(Counter(nums).items(), key=lambda x: -x[1])[:k]]