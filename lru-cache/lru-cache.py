class LRUCache:

    def __init__(self, capacity: int):
        self.k = capacity
        self.LRU = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.LRU:
            self.LRU.move_to_end(key)
        return self.LRU.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self.LRU[key] = value
        self.LRU.move_to_end(key)
        
        if len(self.LRU) > self.k:
            self.LRU.popitem(False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)