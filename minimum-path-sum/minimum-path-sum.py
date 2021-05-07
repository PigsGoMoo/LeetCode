class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for row in grid]
        
        for row in range(len(grid) - 1, -1, -1):
            for col in range(len(grid[0]) - 1, -1, -1):
                if row == len(grid) - 1 and col != len(grid[0]) - 1:
                    dp[row][col] = grid[row][col] + dp[row][col + 1]
                
                elif col == len(grid[0]) - 1 and row != len(grid) - 1:
                    dp[row][col] = grid[row][col] + dp[row + 1][col]
                    
                elif col != len(grid[0]) - 1 and row != len(grid) - 1:
                    dp[row][col] = grid[row][col] + min(dp[row + 1][col], dp[row][col + 1])
                    
                else:
                    dp[row][col] = grid[row][col]
                    
                    
        return dp[0][0]