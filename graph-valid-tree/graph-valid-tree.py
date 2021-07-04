class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree is a single connected, acyclic graph
        # This means that the number of edges needs to be n-1
        # If it's higher, that means we have a cycle. 
        # If it's less, that means it's not connected
        # Lastly, we need to make sure all nodes can be reached from the root node, 0, in this case.
        # Can do this with DFS
        # Another way to do this is union find. You should only get one head
        # You can detect cycles in UF by making sure all unions connect different heads.
        
        # DFS method
        
        
        # UF method
        
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            
            return UF[x]
        
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            
            if UF[find(x)] == UF[find(y)]:
                return False
            
            UF[find(x)] = find(y)
            return True
        
        
        # Base case
        if n == 1:
            return True
        
        for x, y in edges:
            if not union(x, y):
                return False
            
            
        return len({find(x) for x in UF}) == 1 and len(UF) == n