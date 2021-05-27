class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Live cells with 2 - 3 live neighbors live. All else die.
        # Dead cells with exactly 3 live neighbors become live
        # To solve the problem in place, we can mutate the array
        # If something was alive (1) and is now dead (0), we can change
        # the value to something else instead of 0 and have an extra
        # conditional to take care of that value as if it was still 1
        # but then change it to 0 after all nodes have been processed.
        # Likewise, if something was dead and is now alive, we can use
        # a value other than the previous one for the same purpose. 
        
        # Initialize
        num_row = len(board)
        num_col = len(board[0])
        
        # Helper func to update the cell by checking its neighbors
        def update(row, col, living):
            # Count living neighbors
            count = 0
            space = (row, col)
            # Need to check in all eight directions
            # Can do in nested for loop
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    # If we're not in the current spot and still within bounds
                    if (i, j) != space and 0 <= i < num_row and 0 <= j < num_col:
                        if abs(board[i][j]) == 1:
                            count += 1
            
            # Living stays alive if 2-3 neighbors are alive around it
            if living:
                if 2 <= count <= 3:
                    # If living and staying alive, no change
                    return 1
                # Otherwise die
                else:
                    # If living to dead, return -1
                    return -1
            # Dead stays dead unless exactly 3 alive around it
            else:
                # If dead to alive, return 2, otherwise no change
                return 2 if count == 3 else 0
        
        
        for r in range(num_row):
            for c in range(num_col):
                # If board value is originally alive, it's 1.
                if abs(board[r][c]) == 1:
                    board[r][c] = update(r, c, True)
                else:
                    board[r][c] = update(r, c, False)
                    
        # At the end, go through the board again and replace -1 with 0 and 2 with 1
        for r in range(num_row):
            for c in range(num_col):
                if board[r][c] == -1:
                    board[r][c] = 0
                    
                elif board[r][c] == 2:
                    board[r][c] = 1
                    
        # Then we can return
        return board
                    