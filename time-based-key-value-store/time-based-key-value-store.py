class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:      
        # Cuz timestamp is strictly increasing, as in constraints. Otherwise would need to bin search location to put
        self.table[key].append([timestamp, value])            

    def get(self, key: str, timestamp: int) -> str:
        arr = self.table[key]
        n = len(arr)
        
        left = 0
        right = n
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid
        
        return "" if right == 0 else arr[right - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)