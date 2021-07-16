class Solution:
    
    def __init__(self):
        self.board = [[]]
        self.n_row = 0
        self.n_col = 0
        
    def count_mines(self, row, col):
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < self.n_row and 0 <= c < self.n_col and self.board[r][c] == "M":
                    count += 1
                    
        return count
                    
        
    def reveal(self, row, col):
            if self.board[row][col] == "M":
                self.board[row][col] = "X"
                return self.board
            
            elif self.board[row][col] == "E":
                # Count number of mines around
                count = self.count_mines(row, col)
                if count:
                    self.board[row][col] = str(count)
                else:
                    self.board[row][col] = "B"
                    # Now we need to reveal all around it - U UR R DR, D DL, L UL
                    # They want corners, too, it seems
                    dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
                    for dy, dx in dirs:
                        new_row = row + dy
                        new_col = col + dx
                        # If within bounds
                        if 0 <= new_row < self.n_row and 0 <= new_col < self.n_col:
                            # and not yet visited
                            if self.board[new_row][new_col] == "E":
                                self.reveal(new_row, new_col)
                            
        
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.board = board
        self.n_row = len(board)
        self.n_col = len(board[0])
        
        self.reveal(click[0], click[1])
        
        return self.board
        
        
            