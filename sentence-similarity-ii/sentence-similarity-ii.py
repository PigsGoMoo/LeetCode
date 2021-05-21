class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        # Need to make a graph to combine like words
        # Need to have same length and have same heads at every point
        
        # Initialize
        n1 = len(words1)
        n2 = len(words2)
        UF = {}
        
        # Edge cases
        if n1 != n2:
            return False
        
        # Make find func
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
                
            return UF[x]
        
        
        # Make union func
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        
        # Need to make unions for each pair now
        for x, y in pairs:
            union(x, y)
            
        # Now just iterate through both sentences and check to make sure both at the same index are same head
        for i in range(n1):
            if words1[i] in UF and words2[i] in UF:
                if find(words1[i]) != find(words2[i]):
                    return False
                
            else:
                if words1[i] != words2[i]:
                    return False
            
        # Return True outside of for loop
        return True