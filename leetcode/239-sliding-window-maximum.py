class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ret = []
        heap = []
        for idx, num in enumerate(nums[:k-1]):
            heap.append((-num, idx))
        heapify(heap)
        for i in range(k-1, n):
            while heap and heap[0][1] <= i-k:
                heappop(heap)
            heappush(heap, (-nums[i], i))
            ret.append(-heap[0][0])

        return ret
