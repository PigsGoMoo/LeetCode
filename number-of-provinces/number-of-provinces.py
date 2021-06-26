class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Use UF to find number of provinces
        # Each different province will have a different head
        
        # Initialize graph
        UF = {}
        
        # UF Find func
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
                
            return UF[x]
        
        
        # UF union func
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            
            UF[find(x)] = find(y)
            
        
        # Iterate through graph and make a UF graph
        for point_idx, points in enumerate(isConnected):
            # At each index of points, make union if the point is 1
            for connect_idx, point in enumerate(points):
                # If the point is a 1, we union connect_idx with point_idx
                if point == 1:
                    union(connect_idx, point_idx)
                    
        # After all this, the answer is the number of heads
        return len({find(x) for x in UF})
        