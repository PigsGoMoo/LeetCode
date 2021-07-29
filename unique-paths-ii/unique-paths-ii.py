class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # Edge cases
        if (len(obstacleGrid) == 1 and 1 in obstacleGrid[0]):
            return 0
        
        if len(obstacleGrid[0]) == 1:
            for row in obstacleGrid:
                if 1 in row:
                    return 0
                
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Initialize dynamic programming array
        dp = [[0] * len(obstacleGrid[0]) for row in obstacleGrid]

        # Set the first value to 1 if it's not an obstacle. 
        # 0 if it is. (although this should already be covered in edge cases.)
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        
        # Loop through every cell and determine number of unique paths.
        # Number = sum of paths in dp[r-1][c] and dp[r][c-1]
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                # If it's an obstacle, set to 0 because no unique paths can get there
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    
                # Ignore the first cell. We've already set it and we'll be building on from there
                elif r == 0 and c == 0:
                    continue
                    
                # If we're in the first row, number of unique paths is the same as the one in the previous column of
                # same row. This way, if there's an obstacle, the rest of it will be 0
                elif r == 0 and c > 0:
                    dp[r][c] = dp[r][c-1]
                        
                # Same applies to first column
                elif c == 0 and r > 0:
                    dp[r][c] = dp[r-1][c]
                 
                # Otherwise, we just find the sum we mentioned above. 
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
          
        return dp[r][c]