class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        n_row = len(grid)
        n_col = len(grid[0])
        
        ans = 0
        row_hits = 0
        col_hits = [0] * n_col
        
        for row in range(n_row):
            for col in range(n_col):
                # If previous was a wall, reset counter
                # Find number of hits in row
                if col == 0 or grid[row][col - 1] == "W":
                    row_hits = 0
                    # Count how many hits in the row
                    for k in range(col, n_col):
                        # Stop at wall
                        if grid[row][k] == "W":
                            break
                        # Add if enemy
                        elif grid[row][k] == "E":
                            row_hits += 1
                
                # Reset if at top or if previous row was wall
                # Find number of hits in column
                if row == 0 or grid[row - 1][col] == "W":
                    col_hits[col] = 0
                    
                    for k in range(row, n_row):
                        # stop at wall
                        if grid[k][col] == "W":
                            break
                        elif grid[k][col] == "E":
                            col_hits[col] += 1
                            
                # If empty cell, count hits
                if grid[row][col] == '0':
                    total_hits = row_hits + col_hits[col]
                    ans = max(ans, total_hits)
                    
        return ans