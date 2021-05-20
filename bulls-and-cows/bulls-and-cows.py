class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        seen = {}
        
        for num in secret:
            seen[num] = seen.get(num, 0) + 1
        
        n = len(guess)
        
        bull = 0
        cow = 0
        correct = {}
        # Loop through - first pass will get all the bulls.
        for i in range(n):
            # If same, increase bull
            if secret[i] == guess[i]:
                bull += 1
                # Decrease the seen
                seen[secret[i]] -= 1
                # Add to correct
                correct[i] = secret[i]
                
        # Second pass will get the cows
        for i in range(n):
            # If we've already marked it as a bull, we do nothing
            # Otherwise, we see if it's a cow or not
            if i not in correct:
                num = guess[i]
                # If it's a seen value and there are some left
                if seen.get(num, 0) > 0:
                    # Increase cow
                    cow += 1
                    # Decrease seen amt
                    seen[num] -= 1
                    
                    
        return "{}A{}B".format(bull, cow)
                
                
        # Problem: this won't work properly if guess value comes before seen.
        # Ex: secret: 0123 guess: 1023
        # We're supposed to return 2A2B, but we'll actually return 2A1B because 1 in guess comes before 1 in secret, so it
        # won't be seen yet. 
        # To fix, add seen first with index values to map.