class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n_row = len(board)
        n_col = len(board[0])
        
        def search(row, col, idx, word, visited):
            if idx == len(word):
                return True
            
            moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            visited.add((row, col))
            for dy, dx in moves:
                r = row + dy
                c = col + dx
                if 0 <= r < n_row and 0 <= c < n_col:
                    if board[r][c] == word[idx] and (r, c) not in visited:
                        if search(r, c, idx + 1, word, visited):
                            return True
                        
            visited.remove((row, col))
            return False
        
        
        for rowz in range(n_row):
            for colz in range(n_col):
                if board[rowz][colz] == word[0]:
                    if search(rowz, colz, 1, word, set()):
                        return True
                    
        return False
                    
                        