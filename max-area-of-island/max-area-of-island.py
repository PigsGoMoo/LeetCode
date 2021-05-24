class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Idea is to iterate through each value of the grid
        # If I hit land, I check to see the size of that land
        # Then continue until end of grid
        
        # Initialize
        largest = 0
        num_row = len(grid)
        num_col = len(grid[0])
        
        # Recursive function to check size of land. Will take current space and return land size
        # Will also mutate grid and change any visited space to "V"
        def count(row, col):
            # Base case
            if grid[row][col] != 1:
                return 0
            
            # Mutate
            grid[row][col] = "V"
            
            # Check all directions for land
            up = right = down = left = 0
            # Check above
            if row > 0:
                up = count(row - 1, col)
            # Check right
            if col + 1 < num_col:
                right = count(row, col + 1)
            # Check down 
            if row + 1 < num_row:
                down = count(row + 1, col)
            # Check left
            if col > 0:
                left = count(row, col - 1)
            
            # Return value
            return up + right + down + left + 1
        
        
        # Iterate through the grid
        for row in range(num_row):
            for col in range(num_col):
                # If we hit land, call recursion
                if grid[row][col] == 1:
                    # I'll have the recursive func return island size
                    size = count(row, col)
                    # Update largest if needed
                    largest = max(largest, size)
                    
                    
        # At end of loop, we'll have gone through everything, so return
        return largest