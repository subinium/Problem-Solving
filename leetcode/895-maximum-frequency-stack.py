class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(lambda: 0)
        self.heap = []
        self.idx = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.idx += 1
        heappush(self.heap, (-self.cnt[val], -self.idx, val))

    def pop(self) -> int:
        _, _, val = heappop(self.heap)
        self.cnt[val] -= 1
        return val
