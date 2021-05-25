class SnapshotArray:

    # Works but inefficient because O(n) every time you snap
    # Instead, we can use a binary search to find the get and save only
    # the changed index when we snap
    def __init__(self, length: int):
        self.arr = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Binary search for the snap_id
        arr = self.arr[index]
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid][0] > snap_id:
                right = mid - 1
                
            else:
                left = mid + 1
                
        return self.arr[index][right][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)