class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Can do string manipulation and solve easily
        # Can save space and use bit manipulation instead
        
        # Initialize variables
        n_bytes = 0
        
        # This mask is used to check the second to left most bit in following bytes because they need
        # to be 0. So this with AND should result in 0.
        mask2 = 1 << 6
        
        for num in data:
            # This mask used for left most value
            mask = 1 << 7
            
            # So if we're dealing with the first byte in the sequence
            if n_bytes == 0:
                # While the mask returns 1 (aka the value we're checking is 1) or less than 5 bytes
                while mask & num and n_bytes < 5:
                    # Increase n_bytes
                    n_bytes += 1
                    # Shift mask to right by 1.
                    mask = mask >> 1
                    
                # If we're dealing with a 1 byte char
                if n_bytes == 0:
                    continue
                    
                # If invalid (invalid if one counted or more than 4 bytes. One byte starts with 0, not 1)
                if n_bytes == 1 or n_bytes > 4:
                    return False
                
            # Otherwise, we're dealing with a byte that isn't the first in the sequence
            else:
                # Just need to check if two leftmost bits == 10
                # If not, it's not valid
                if not (num & mask and not (num & mask2)):
                    return False
                
            n_bytes -= 1
        
        # Outside the for loop, we need to make sure no bytes are left. 
        return n_bytes == 0