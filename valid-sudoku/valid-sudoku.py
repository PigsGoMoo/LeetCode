class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First try at solution. Not as efficient
#         def checkRow(row, column):
#             for i in range(len(board[row])):
#                 if board[row][i] == board[row][column] and i != column:
#                     return False
                
#             return True
        
        
#         def checkColumn(row, column):
#             for i in range(len(board)):
#                 if board[i][column] == board[row][column] and i != row:
#                     return False
                
#             return True
        
        
#         def checkBox(row, column):
#             rowBox = row // 3  # Should give me 0/1/2
#             columnBox = column // 3
            
#             for rowz in range(3 * rowBox, 3 * (rowBox + 1)):  # Should start from beginning of box to start of next one
#                 for col in range(3 * columnBox, 3 * (columnBox + 1)):
#                     if board[rowz][col] == board[row][column] and rowz != row and col != column:
#                         return False
            
#             return True
        
        
#         for row in range(len(board)):
#             for col in range(len(board[0])):
#                 if board[row][col] != ".":
#                     if not checkRow(row, col) or not checkColumn(row, col) or not checkBox(row, col):
#                         return False
                    
#         return True
            
        # Can use hash tables to make this even more efficient.
        
        # Initialize hash tables. It's inside an array so we can access the data 
        # by corresponding it to the row/column it belongs
        
        # We can't just do [{}] * 9 because that makes copies and hash is copied by reference.
        # So modifying it will modify all
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    num = int(num)
                    # We index boxes from 0 to 8 going from left to right, up to down.
                    # The formula to find which index a number is in is:
                    # (row // 3) * 3 + j // 3
                    # Row // 3 will give you 0/1/2. Multiply by 3 to give you which boxRow you have.
                    # Add on j // 3 to decide which boxColumn you have.
                    box_index = (row // 3) * 3 + col // 3
                    
                    # Store value in hash
                    rows[row][num] = rows[row].get(num, 0) + 1
                    columns[col][num] = columns[col].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # Check if it's been put in a row/column/box before
                    if rows[row][num] > 1 or columns[col][num] > 1 or boxes[box_index][num] > 1:
                        return False
                    
        return True
    