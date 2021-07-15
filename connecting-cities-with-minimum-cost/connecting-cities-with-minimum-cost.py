class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # Use union find to make the connections.
        # Sort by increasing weights and greedily make connections. 
        # If connection already made, don't make a new one
        
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
                
            return UF[x]
        
        
        def union(x, y):
            
            if weights[x] > weights[y]:
                UF[find(y)] = find(x)
                weights[x] += weights[y]
                
            else:
                UF[find(x)] = find(y)
                weights[y] += weights[x]
                
        
        # Start off by sorting connections by its weights
        connections.sort(key = lambda x: x[2])
        
        # Initialize variable to keep track of total connections and current cost
        total = 0
        cost = 0
        # Weights will start off as 1 for each node. Nodes are 1 indexed
        weights = [1] * (n+1)
        # Look through each connection and make the connections if not already made
        for x, y, weight in connections:
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            if find(x) != find(y):
                union(x, y)
                cost += weight
                total += 1
                
        # If all of our nodes are connected, we'll have a total of n-1 edges, otherwise, not all can be connected
        return cost if total == n-1 else -1
        