class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        # Start with all rotten ones at time 0
        # Add on all adjacent with time + 1
        # keep seen tracker
        # go until queueueuueuee is empty
        
        q = collections.deque()
        n_row = len(grid)
        n_col = len(grid[0])
        rotten = set()
        fresh = 0
        # First find all initally rotten ones and add to queueueueue
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                if grid[r][c] == 1:
                    fresh += 1
        
        # Now make everything rotten spreading out and adding to q if it's a 1 and not in rotten
        # Don't need to add 2 to rotten since we're not mutating
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # R D L U
        ans = 0
        rot = 0
        while q:
            r, c, time = q.popleft()
            if time > ans:
                ans = time
            for dy, dx in dirs:
                dr = dy + r
                dc = dx + c
                if 0 <= dr < n_row and 0 <= dc < n_col and grid[dr][dc] == 1 and (dr, dc) not in rotten:
                    q.append((dr, dc, time + 1))
                    rot += 1
                    rotten.add((dr, dc))
            
        return ans if rot == fresh else -1
        