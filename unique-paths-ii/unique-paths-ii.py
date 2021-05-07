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
        
        
        dp = [[0] * len(obstacleGrid[0]) for row in obstacleGrid]

        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        
        print(dp)
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    
                elif r == 0 and c == 0:
                    continue
                    
                elif r == 0 and c > 0:
                    dp[r][c] = dp[r][c-1]
                        
                elif c == 0 and r > 0:
                    dp[r][c] = dp[r-1][c]
                    
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
          
        return dp[r][c]