class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Idea is that if it's possible to swap and get all on one side, 
        # then it has to be one of the values in the first domino. 
        # So we'll check and see if the value can be swapped or not.
        # Then return the min swaps
        
        # Helper func to count number of rotations
        def rotator(x):
            # Initialize
            res_a = res_b = 0
            # Iterate through the arrays
            for i in range(n):
                # If top and bottom values don't have the value we want, 
                # Then we won't be able to get our result, so return -1
                if tops[i] != x and bottoms[i] != x:
                    return -1
                
                # If top value is x and bottom is not:
                elif bottoms[i] != x:
                    # Then we need to rotate the bottom one
                    res_b += 1
                    
                # If bottom == x and top != x
                elif tops[i] != x:
                    # Then rotate top
                    res_a += 1
                    
            # Answer will be the one with less rotations
            return min(res_a, res_b)
        
        
        n = len(tops)
        ans = rotator(tops[0])
        
        # If we found an answer, return it
        # Or if the two values are the same - we've already checked it, so return what we have
        if ans != -1 or tops[0] == bottoms[0]:
            return ans
        # Otherwise, check the bottom value. If that doesn't find it, then we can't anyway. So return from there.
        else:
            return rotator(bottoms[0])
                