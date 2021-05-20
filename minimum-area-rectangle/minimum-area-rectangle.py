class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        
        # Edge case - no rectangles can be made.
        if nx == n or ny == n:
            return 0
        
        point_map = collections.defaultdict(list)
        
        # Grab list of points with same x or y value based on whichever one has more
        # Because we'll eventually loop through every possible combination in this array,
        # we want it to have as little values as possible. So if we have more x values,
        # We'll make the array from the y values. 
        if nx > ny:
            for x, y in points:
                point_map[x].append(y)
                
        else:
            for x, y, in points:
                point_map[y].append(x)
                
        # This hash will hold the very last x value we've seen for any y1, y2 pair with the same x value
        # Because the smallest area of the rectangle in a sorted list of x values is the current + the last one
        # we saw. So we can "forget" any that we've seen before that because those areas will be larger.
        lastx = {}
        
        ans = float('inf')
        
        # Sort x values from lowest to highest then iterate through them
        for x in sorted(point_map):
            # Sort the y values because lower values = less area
            point_map[x].sort()
            # Loop through each of those y values
            for i in range(len(point_map[x])):
                # Loop up to that point for possible combos
                for j in range(i):
                    # Initialize variables
                    y1, y2 = point_map[x][i], point_map[x][j]
                    
                    # If we've seen this combo of y values with a different x value before,
                    # then we can make a rectangle from this
                    if (y1, y2) in lastx:
                        # Calculate area and choose lesser value
                        ans = min(ans, (x - lastx[y1, y2]) * abs(y1 - y2) )
                        
                    # Then set this into the lastx
                    lastx[y1, y2] = x
                    
        return ans if ans < float('inf') else 0