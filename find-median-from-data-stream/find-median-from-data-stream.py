class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.sorted = False
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.sorted = False

    def findMedian(self) -> float:
        if not self.sorted:
            self.arr.sort()
            self.sorted = True
        
        n = len(self.arr)
        
        if n % 2:
            return self.arr[(n) // 2]
        
        else:
            mid = n // 2
            return (self.arr[mid] + self.arr[mid - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()