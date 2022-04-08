class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hq = nums[:(min(k, len(nums)))]
        heapq.heapify(self.hq)
        for i in range(k, len(nums)): self.add(nums[i])

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        while len(self.hq) > self.k: heapq.heappop(self.hq)
        return self.hq[0]
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)