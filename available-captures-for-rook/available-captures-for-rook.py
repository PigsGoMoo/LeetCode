class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Idea is to search for rook. Then go out in all four directions until hit another piece or edge
        
        # Search for rook
        for Row in range(8):
            for Col in range(8):
                if board[Row][Col] == "R":
                    row = Row
                    col = Col
                    # Once we find it, since there's only one, we can exit the for loop
                    break
                    
        
        # Now we check in all four directions until we hit another character
        
        # We can do this with a for loop for the directions and a while loop to traverse that direction until edge
        # Delta determines the direction we go in. 1,0 is to go down. Then left, up, right.
        delta = [[1,0], [0, -1], [-1, 0], [0, 1]]
        ans = 0
        
        # Loop through
        for delta_row, delta_col in delta:
            # Our initial values because we don't want to start at the rook's position
            new_row = row + delta_row
            new_col = col + delta_col
            
            # Traverse that direction until we hit an edge. 
            # Edge of chess board is at 8
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                # If we find a pawn, increment ans
                if board[new_row][new_col] == "p":
                    ans += 1
                    # Then we can exit the while loop because we can't hit more than one pawn
                    break
                # If we hit anything but empty space (like a bishop), we also exit
                elif board[new_row][new_col] != ".":
                    break
                    
                # Otherwise, if it is an empty space, we keep iterating
                else:
                    new_row += delta_row
                    new_col += delta_col
                    
        
        # Return ans
        return ans
                    
        