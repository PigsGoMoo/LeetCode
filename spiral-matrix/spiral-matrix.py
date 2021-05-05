class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Initialize answer array
        ans = []
        
        # Edge cases
        if not matrix:
            return ans
        
        # Calculate how many total cells there are
        Row = len(matrix)
        Col = len(matrix[0])
        Tot = Row * Col
        
        # Initialize a matrix to keep track of which cells we've visited already
        seen = [[False] * Col for rows in matrix]
        
        # Arrays to determine which direction to move the pointer
        # In the beginning, we go right, so row doesn't change but col changes by +1
        # Then we head down, so row changes by +1 and col doesn't change
        # Then left, so row doesn't change and col changes by -1
        # Lastly, back up, so row changes -1 and col doesn't change.
        # Then repeat back at index 0.
        deltaRow = [0, 1, 0, -1]
        deltaCol = [1, 0, -1, 0]
        
        # Initialize indices. 
        row = col = deltaIdx = 0
        
        # Loop through every cell
        for _ in range(Tot):
            
            # Add to ans array
            ans.append(matrix[row][col])
            
            # Mark as seen
            seen[row][col] = True
            
            # New index values.
            changeRow = row + deltaRow[deltaIdx]
            changeCol = col + deltaCol[deltaIdx]
            
            # If new values are within bounds of the matrix and not visited yet, set row/col to these
            if 0 <= changeRow < Row and 0 <= changeCol < Col and not seen[changeRow][changeCol]:
                row = changeRow
                col = changeCol
                
            # Otherwise, increase deltaIdx (aka a counterclockwise turn) and set new row/col values
            else:
                deltaIdx = (deltaIdx + 1) % 4
                row += deltaRow[deltaIdx]
                col += deltaCol[deltaIdx]
        
        # By end of for loop, we should be done.
        return ans