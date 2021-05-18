class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.idx = 0
        self.next_val = []
        
        i = 0
        
        while i < min(len(v1), len(v2)):
            self.next_val.append(v1[i])
            self.next_val.append(v2[i])
            i += 1
            
        self.next_val.extend(v1[i:] if i < len(v1) else v2[i:])

    def next(self) -> int:
        
        res = self.next_val[self.idx]
        self.idx += 1
        
        return res

    def hasNext(self) -> bool:
        return self.idx < len(self.next_val)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())