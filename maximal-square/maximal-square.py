class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
#         # Start from top left
#         # If hit 1, slowly expand down + right. No need to check other directions
#         # Keep track of highest area
        
#         def check(row, col, curr_max):
#             # Will keep expanding and updating until broken out of
#             r = row
#             c = col
#             curr_width = 1
#             # Expand to be size of previous max. If it can't, it's not bigger anyway
#             while True:                
#                 # Expand right first
#                 # If we can't just end it here
#                 if c + 1 < n_col and matrix[r][c + 1] != "1":
#                     return curr_width
                
#                 # If we can, then check that everything in the new expansion is a 1
#                 for i in range(row, r + 2):
#                     # If we're out of bounds, that means we don't have enough to make another square
#                     # So just return right away
#                     if i == n_row:
#                         return curr_width
#                     for j in range(col, c + 2):
#                         if j == n_col:
#                             return curr_width
#                         # If it's not, then we can just return the current area
#                         if matrix[i][j] != "1":
#                             return curr_width
                
#                 # If we make it out of that for loop, that means everything is a 1, so we increment 
#                 # and start again
#                 r += 1
#                 c += 1
#                 curr_width += 1
        
        
#         n_row = len(matrix)
#         n_col = len(matrix[0])
#         ans = 0
        
#         for r in range(n_row):
#             for c in range(n_col):
#                 if matrix[r][c] == "1":
#                     ans = max(ans, check(r, c, ans))
                    
#         return ans * ans
        
        # Can be improved with dynamic programming. We keep track of max size of box where dp[r][c] is the
        # size of the box, with this point being the bottom right corner of it
        # We can get this value by adding 1 to the min(dp[i - 1][j], dp[i][j-1], dp[i-1][j-1])
        # basically the previous box, box above, and box to top left. If any of these are 0, then 
        # the only box we can make is of size 1.
        
        n_row = len(matrix)
        n_col = len(matrix[0])
        dp = [[0] * n_col for i in range(n_row)]
        ans = 0
        
        for r in range(n_row):
            for c in range(n_col):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    ans = max(ans, dp[r][c])
                    
        return ans * ans
        
        