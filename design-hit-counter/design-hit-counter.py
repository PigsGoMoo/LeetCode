class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # We'll store timestamp, hit count as an array inside a queueuueueueue
        # If timestamp difference between newly added and top element is > 300, we can remove it
        # cuz constraint says it's always increasing
        # We'll also have a total to keep track of the total inside of the queueueue instead of calculating it every time
        self.q = collections.deque()
        self.tot = 0
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # If timestamp isn't already in there, add it
        if not self.q or self.q[-1][0] != timestamp:
            self.q.append([timestamp, 1])
        # If it is, increment the hit count by 1
        else:
            self.q[-1][1] += 1
        
        # Increment total
        self.tot += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
                
        # Remove any values more than 5 min away
        while self.q and timestamp - self.q[0][0] >= 300:
            hits = self.q.popleft()[1]
            self.tot -= hits
            
        return self.tot
        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)