class Solution:
    def findContestMatch(self, n: int) -> str:
        
        # Helper func to format string
        def format_string(first, second):
            return "({},{})".format(first, second)
        
        # Make initial array
        teams = [i for i in range(1, n + 1)]
        
        n_team = len(teams)
        
        left = 0
        right = n_team - 1
        # Loop through array by twos and combine them strongest + weakest
        while right > 0:
            # Combine left most with right most
            while left < right:
                # Combine it into the left most arr
                teams[left] = format_string(teams[left], teams[right])
                # Increment pointers
                left += 1
                right -= 1
                
            # At the end of the while loop, right should be where it belongs.
            # Left needs to move
            left = 0
            
        return teams[0]
                
            