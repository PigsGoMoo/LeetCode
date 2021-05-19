class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # Brute force solution. Not time efficient
#         ptr = 0
#         ans = 0
#         n = len(sentence)
        
#         # Go through rows
#         for i in range(rows):
#             col = cols            
#             while col > 0:
                
#                 # If word fits, put in word
#                 if len(sentence[ptr]) <= col:
#                     col -= len(sentence[ptr])
#                     ptr += 1
                    
#                     # If pointer is past the last index, reset + increase count
#                     if ptr == n:
#                         ptr = 0
#                         ans += 1
                        
#                     # Add the space if 2 or more spots left cuz a single letter word can fit.
#                     if col > 1:
#                         col -= 1
                    
#                     # If there's only 1 or 0 left, nothing else can fit (cuz space takes 1)
#                     else:
#                         break
                        
#                 # If word doesn't fit, move into next line
#                 else:
#                     break
        
#         return ans
        # Initialize pointer and combine sentence into one string
        ptr = 0
        s = " ".join(sentence) + " "
        n = len(s)
        
        # Iterate through the rows
        for i in range(rows):
            # Add number of columns to pointer
            ptr += cols - 1
        
            # If this ends at a space, increment to the next word
            # We need to do modulo here because pointer might wrap around
            if s[ptr % n] == " ":
                ptr += 1
            
            # If it ends at the very end of the word, increment to next word
            elif s[(ptr + 1) % n] == " ":
                ptr += 2
                
            # Else, it will end at the middle of the word,
            # In which case, we need to decrement to start of the word
            else:
                # So while we're not at the beginning and while we're in the middle of a word
                while (ptr - 1) % n >= 0 and s[(ptr - 1) % n] != " ":
                    ptr -= 1

        # Once the foor loop exits, we now know where the pointer is. 
        # To figure out how many times it's been done, we just do floor division
        return ptr // n
        
            
