class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        
        board = []
        queen_locations = []
        
        for row in range(n):
            board.append([])
            for col in range(n):
                board[row].append(1)
                
        
        def backtrack(row, count):
            
            for col in range(n):
                if board[row][col]:
                    if board[row][col] != "Q":
                        place_queen(row, col)
                        # print("Queen placed at {}, {}. Board is: \n{}".format(row, col, board))
                        if row + 1 == n:
                            print("Incrementing count for the current answer: {}".format(queen_locations))
                            print("Current board: {}".format(board))
                            count += 1
                        
                        else:
                            count = backtrack(row + 1, count)
                        
                        remove_queen(row, col)
            print("Returning count: {}".format(count))
            return count
        
        
        def place_queen(row, col):
            # Need to change all values in same row + col to 0 
            # Then same with the diagonals
            
            # Make row 0
            for i in range(n):
                board[i][col] = 0
                
            # Make col 0
            for j in range(n):
                board[row][j] = 0
                
            # Deal with diagonals
            i = 1
            j = 1
            
            # Going up + left
            while row - i >= 0 and col - j >= 0:
                board[row - i][col - j] = 0
                i += 1
                j += 1
                
            j = 1
            i = 1
            # Down + right
            while row + i < n and col + j < n:
                board[row + i][col + j] = 0
                i += 1
                j += 1
                
            i = 1
            j = 1
            # Up + right
            while row - i >= 0 and col + j < n:
                board[row - i][col + j]
                i += 1
                j += 1
                
            # Down + left
            i = 1
            j = 1
            while row + i < n and col - j >= 0:
                board[row + i][col - j] = 0
                i += 1
                j += 1
            
            # Mark the queen
            board[row][col] = "Q"
            if [row, col] in queen_locations:
                return
            queen_locations.append([row, col])
            
            print("Queen added at {}, {}".format(row, col))
            print(board)
            # print(queen_locations)
                
            
        def remove_queen(row, col):
        #     # Need to change 0 back to 1 IF no other queen has influence on the space...
            queen_locations.remove([row, col])
            
            print("Queen removed from position {}, {}".format(row, col))
            # print(queen_locations)
            
            for row in range(n):
                for col in range(n):
                    board[row][col] = 1
            for row, col in queen_locations:
                place_queen(row, col)
        
        count = backtrack(0, 0)
        return count
    
            