class Solution:
    def calculate(self, s: str) -> int:
        
        # Initialize variables
        ans = 0
        sign = 1
        curr = 0
        stack = []
        
        # Iterate through each character in s
        for char in s:
            # If it's a number, we need to add it to curr. 
            # Remember the number can have multiple digits
            if char in '1234567890':
                curr = curr*10 + int(char)
            
            # If it's not a number, but rather a + sign
            elif char == '+':
                # Add our current value to our running sum
                ans += sign * curr
                sign = 1
                # and reset curr
                curr = 0
                
            # If it's a minus sign, do same thing but change our sign
            elif char == '-':
                ans += sign * curr
                sign = -1
                curr = 0
                
            # If it's an open parenthess
            elif char == '(':
                # We need to start our stack
                # We'll add our current running sum and current sign into stack in that order
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
                
            # Evaluate as normal until we hit the close
            elif char == ')':
                
                # Finish evaluating everything to the left first
                ans += sign * curr
                curr = 0
                
                # Now we need to pop the last two items from stack
                # First item will be the sign (because it was the last one we added)
                # Second will be our running sum
                ans *= stack.pop()
                ans += stack.pop()                
                
        return ans + sign * curr
        