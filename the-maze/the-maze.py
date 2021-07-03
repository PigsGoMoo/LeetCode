class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Can use BFS or DFS.
        # Idea is that each path is like a tree/graph structure where you can traverse until you find 
        # a node you've already visited (meaning any further repetitions will have already been accounted for)
        # or destination.
        
        # DFS
        # Make a dfs function to traverse and visited array to see if we've been there or not
        # It'll take in the start location, destination, and visited matrix
        def dfs(start, dst, visited):
            
            # Initialize
            n_row = len(maze)
            n_col = len(maze[0])
            row = start[0]
            col = start[1]
            
            # Base cases
            # If already visited
            if visited[row][col]: return False
            
            # If reached destination
            if row == dst[0] and col == dst[1]: return True
            
            # Mark node as visited
            visited[row][col] = True
            
            # Make new variable for iteration in each direction
            # Right/Left is incrementing/decrementing column. Up/Down is decre/incrementing row
            r = l = col
            u = d = row
            
            # Go right + recurse
            # While not at edge and still path
            while r + 1 < n_col and maze[row][r + 1] == 0:
                r += 1
            
            if dfs([row, r], dst, visited):
                return True
            
            # Go left and recurse
            while l - 1 >= 0 and maze[row][l - 1] == 0:
                l -= 1
                
            if dfs([row, l], dst, visited):
                return True
            
            # Go up and recurse
            while u - 1 >= 0 and maze[u - 1][col] == 0:
                u -= 1
                
            if dfs([u, col], dst, visited):
                return True
            
            # Go down and recurse
            while d + 1 < n_row and maze[d + 1][col] == 0:
                d += 1
                
            if dfs([d, col], dst, visited):
                return True
            
            # If none of these are true, return False
            return False
        
        
        n_row = len(maze)
        n_col = len(maze[0])
        
        visited = [[False] * n_col for _ in range(n_row)]
        return dfs(start, destination, visited)
        