class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Greedy place into valid sequences if possible
        # If not, return False
        
        # Initialize counter
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Initialize sequences
        # We're gonna use a hash of end values - meaning each value in here is the "last" value
        # in any subarray sequence
        end = {}
        
        # Now we loop through nums array
        for i in nums:
            # First, if we have none of those numbers left (because of greedy method), skip
            if not count[i]: 
                continue
            
            # Check and see if we can place it anywhere
            # Decrement
            count[i] -= 1
            # Two options to place 
            # First is at the end of a currently existing array
            if end.get(i - 1, 0) > 0:
                # Decrement end - 1
                end[i - 1] -= 1
                # Add new end value
                end[i] = end.get(i, 0) + 1
                
            # Second is to make a new array
            # But we need to check if there's a minimum length of 3
            # Or else it won't be valid
            elif count.get(i + 1, 0) > 0 and count.get(i + 2, 0) > 0:
                # So then decrement the counter for the next two numbers in seq
                count[i + 1] -= 1
                count[i + 2] -= 1
                # Then add to end
                end[i + 2] = end.get(i + 2, 0) + 1
                
            # If we can't fit in those two above, then we can say it's not valid
            else:
                return False
            
        return True
            