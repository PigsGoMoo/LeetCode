class Node:
    def __init__(self, val = None):
        self.val = val
        self.neighbors = {}
        self.final = ''


class Solution:
    def __init__(self):
        self.ans = set()
    
    def check_word(self, curr, row, col, board, visited): 
        # curr is current node in trie
        # row, col is position in board
        # Board is our given matrix
        
        # So we need to check each direction to see if that letter is a match to the nextt
        # position in trie
        # Plan on returning the full word in case there are multiple that start with same letter
        n_row = len(board)
        n_col = len(board[0])
        # print("We're currently at [{}, {}] on the board and looking at the letter {} and looking for {}"
        #       .format(row, col, curr.val, curr.neighbors.keys()))
        # Base case
        # If we've hit a word, add that word to our ans array
        
        if (row, col) in visited:
            # print("Already been here")
            return
        
        if curr.final and curr.final not in self.ans:
            # print("We've hit the word {}. Adding it to ans".format(curr.final))
            self.ans.add(curr.final)
        
        # If no more neighbors, we've hit the end of the word
        if not curr.neighbors:
            # print("No more neighbors.")
            return
        
        # Add to visited before exploring
        visited.add((row, col))
        
        r = col + 1
        l = col - 1
        u = row - 1
        d = row + 1
        
        # Check right
        if r < n_col and board[row][r] in curr.neighbors:
            letter = board[row][r]
            # print("We found the letter {} to the right. Recursing into it".format(letter))
            self.check_word(curr.neighbors[letter], row, r, board, visited)
            
        # Check left
        if l >= 0 and board[row][l] in curr.neighbors:
            letter = board[row][l]
            # print("We found the letter {} to the left. Recursing into it".format(letter))
            self.check_word(curr.neighbors[letter], row, l, board, visited)
            
        if u >= 0 and board[u][col] in curr.neighbors:
            letter = board[u][col]
            # print("We found the letter {} above. Recursing into it".format(letter))
            self.check_word(curr.neighbors[letter], u, col, board, visited)
            
        if d < n_row and board[d][col] in curr.neighbors:
            letter = board[d][col]
            # print("We found the letter {} below. Recursing into it".format(letter))
            self.check_word(curr.neighbors[letter], d, col, board, visited)
        
        # print("No other letters found.")
        # Remove from visited after exploring
        visited.remove((row, col))
        return
        
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Make trie
        # Iterate
        # Check for each char where letter = first letter of a word
        trie = Node()
        for word in words:
            curr = trie
            for i in range(len(word)):
                letter = word[i]
                if letter in curr.neighbors:
                    curr = curr.neighbors[letter]
                    continue
                
                curr.neighbors[letter] = Node(letter)
                curr = curr.neighbors[letter]
                
            curr.final = word
                    
        
        # Iterate through matrix
        n_row = len(board)
        n_col = len(board[0])
        
        for r in range(n_row):
            for c in range(n_col):
                # If this letter is in the trie
                letter = board[r][c]
                if letter in trie.neighbors:
                    # Call helper that checks if word is there
                    # print("We found the letter {}. Recursing into it".format(letter))
                    vis = set()
                    self.check_word(trie.neighbors[letter], r, c, board, vis)
                
        return list(self.ans)
        