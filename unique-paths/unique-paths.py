class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Because we can only go right or down, the number of unique paths to get to an area is the
        # sum of the number of paths above it and to left of it
        # As such, we can solve this dynamically
        dp = [[1] * m for _ in range(n)]
        
        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
                
        return dp[n - 1][m - 1]
                