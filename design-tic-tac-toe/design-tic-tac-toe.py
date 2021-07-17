class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        # Logic here is that in order to win, you'd have to mark a single row/column/diagonal/antidiag n times
        # So instead of making a matrix and checking it every time, we just need to keep track of those 4
        # When the number of times hits n, we have a winner
        self.p1 = {
            'row' : [0] * n,
            'col' : [0] * n,
            'diag' : 0, 
            'antidiag' : 0
        }
        
        self.p2 = {
            'row' : [0] * n,
            'col' : [0] * n,
            'diag' : 0, 
            'antidiag' : 0
        }
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        p = self.p1 if player == 1 else self.p2
        # Update row count
        p['row'][row] += 1
        # Update col count
        p['col'][col] += 1
        # Update diag if applicable
        if row == col:
            p['diag'] += 1
        # Update antidiag
        if col == self.n - row - 1:
            p['antidiag'] += 1
        
        # If win
        if p['row'][row] == self.n or p['col'][col] == self.n or p['diag'] == self.n or p['antidiag'] == self.n:
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)