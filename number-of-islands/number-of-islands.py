class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        ans = 0
        
        def visit_island(row, col, num_row, num_col):
            grid[row][col] = "V"
            # Check above if applicable
            if row >= 1 and grid[row-1][col] == '1':
                visit_island(row - 1, col, num_row, num_col)
            # Check left, if applicable
            if col >= 1 and grid[row][col-1] == '1':
                visit_island(row, col-1, num_row, num_col)
            # Check below
            if row + 1 < num_row and grid[row+1][col] == '1':
                visit_island(row + 1, col, num_row, num_col)
            # Check right
            if col + 1 < num_col and grid[row][col+1] == '1':
                visit_island(row, col + 1, num_row, num_col)
            
        
        for row in range(num_row):
            for col in range(num_col):
                if grid[row][col] == "1":
                    ans += 1
                    visit_island(row, col, num_row, num_col)
        
        return ans