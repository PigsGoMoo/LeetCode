import random

class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.res = []
        for prob in w:
            self.total += prob
            self.res.append(self.total)
        

    def pickIndex(self) -> int:
        target = self.total * random.random()
        
        for i, tot in enumerate(self.res):
            if target < tot:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()