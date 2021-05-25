class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        # Initialize
        # Edge cases
        # Group together all the L and Rs in the string with their index
        start_vals = [(s, idx) for idx, s in enumerate(start) if s == "L" or s =="R"]
        end_vals = [(e, idx) for idx, e in enumerate(end) if e=="L" or e == "R"]
        
        # If we don't have the same number of L and R values, then impossible to transform
        if len(start_vals) != len(end_vals):
            return False
        
        # Loop through each pair of corresponding values
        for (s, i), (e, j) in zip(start_vals, end_vals):
            # If they're not equal, we can just return false here
            if s != e:
                return False
            # If it's L, L can only move to the left, so if the L in s appears before
            # the L in e, it doesn't work
            if s == "L" and i < j:
                return False
            
            # Opposite for R, since it can only move right
            if s == "R" and i > j:
                return False
            
        return True