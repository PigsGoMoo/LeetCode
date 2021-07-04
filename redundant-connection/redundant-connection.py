class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Can use union find.
        # If the heads are the same, that means it's a redundant input
        # Return answer that occurs last, so if we continue to loop through in order
        # if we reach a redundant connection, set that connection as answer
        # Otherwise, keep going.
        
        UF = {} 
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
                
            return UF[x]
        
        
        # Will return False if redundant connection
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            
            if find(x) == find(y):
                return False
            
            UF[find(x)] = find(y)
            return True
        
        
        ans = []
        for x, y in edges:
            if not union(x, y):
                ans = [x,y]
        
        return ans
        