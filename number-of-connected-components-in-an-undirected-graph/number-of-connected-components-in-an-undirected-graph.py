class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Can use union find
        
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
                
            return UF[x]
        
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
            
        for i in range(n):
            UF.setdefault(i, i)
            
        for x, y in edges:
            union(x, y)
            
        return len({find(x) for x in UF})
        