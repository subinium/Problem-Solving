class MyHashSet:
    def __init__(self):
        self.s = set()        

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        self.s.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.s


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)