class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # In every group of numbers that are connected by either an x or a y value,
        # We can remove all but one of those
        # So then to answer this question, we can see how many groups we make
        # If we remove all of those groups, one will be left from each. If we subtract
        # the number of groups from the total number of stones, we'll get the value of how
        # many stones we remove
        # We can make the groups by making a disjointed set on the x and y values. 
        
        # Initialize
        UF = {}
        
        # Define the find func
        def find(x):
            # If x isn't equal to its value pair, that means the head of x is in a different place
            # So we need to find the head.
            if x != UF[x]:
                UF[x] = find(UF[x])
                
            return UF[x]
        
        
        # Define union func
        def union(x, y):
            # Initialize values if needed
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            # Join them together
            UF[find(x)] = find(y)
            
        
        # From here, we just need to go through each of the points in stones and call union on them
        for x, y in stones:
            # We call y + 10000 so that we don't accidentally use the same numbers for keys if x == y
            union(x, y + 10000)
            
        # After we have our graph set up, we can count the number of heads in the graph
        islands = {find(x) for x in UF}
        
        return len(stones) - len(islands)