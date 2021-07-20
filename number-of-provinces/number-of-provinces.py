class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         # Use UF to find number of provinces
#         # Each different province will have a different head
        
#         # Initialize graph
#         UF = {}
        
#         # UF Find func
#         def find(x):
#             if x != UF[x]:
#                 UF[x] = find(UF[x])
                
#             return UF[x]
        
        
#         # UF union func
#         def union(x, y):
#             UF.setdefault(x, x)
#             UF.setdefault(y, y)
            
#             UF[find(x)] = find(y)
            
        
#         # Iterate through graph and make a UF graph
#         for point_idx, points in enumerate(isConnected):
#             # At each index of points, make union if the point is 1
#             for connect_idx, point in enumerate(points):
#                 # If the point is a 1, we union connect_idx with point_idx
#                 if point == 1:
#                     union(connect_idx, point_idx)
                    
#         # After all this, the answer is the number of heads
#         return len({find(x) for x in UF})
        
        # UF is O(n^3) worst case. UF itself is O(n) worst case and then matrix traversal is O(n^2)
        
        # DFS version - O(n^2)
        
        # We can simply go through every node. 
        # If it's unvisited, then we can traverse that node and mark everything as visited
        # Then move onto next unvisited node. Every unvisited node is a separate "province"
        
        def dfs(node):
            for i in range(len(isConnected)):
                # If the next node, i, is adjacent to current node and not visited yet
                if isConnected[node][i] == 1 and not visited[i]:
                    # Set to visited
                    visited[i] = True
                    # Then visit
                    dfs(i)
                    
        
        # Visited will just tell us if that node has been visited before or not
        visited = [False] * len(isConnected)
        ans = 0
        
        for i in range(len(isConnected)):
            if not visited[i]:
                # We don't need to set visited here because each node is adjacent to itself, so dfs will handle
                dfs(i)
                ans += 1
                
        return ans
        