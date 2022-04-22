class MyHashMap:
    
    def __init__(self):
        self.dct = [-1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.dct[key] = value

    def get(self, key: int) -> int:
        return self.dct[key]

    def remove(self, key: int) -> None:
        self.dct[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)