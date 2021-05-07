class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize ans array
        ans = [[0] * n for _ in range(n)]
        
        # Initialize other variables
        row = 0
        col = 0
        deltaRow = [0, 1, 0, -1]
        deltaCol = [1, 0, -1, 0]
        deltaIdx = 0
        currVal = 1
        
        for i in range(n**2):
            if ans[row][col] != 0:
                row -= deltaRow[deltaIdx]
                col -= deltaCol[deltaIdx]
                deltaIdx = (deltaIdx + 1) % 4
                row += deltaRow[deltaIdx]
                col += deltaCol[deltaIdx]
                
            ans[row][col] = currVal
            currVal += 1
            if row + deltaRow[deltaIdx] == n or col + deltaCol[deltaIdx] == n:
                deltaIdx = (deltaIdx + 1) % 4
                
            col += deltaCol[deltaIdx]
            row += deltaRow[deltaIdx]
            
        print(ans)        
        return ans
    