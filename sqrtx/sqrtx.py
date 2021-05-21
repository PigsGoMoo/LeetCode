class Solution:
    def mySqrt(self, x: int) -> int:
        # Base case
        if x < 2:
            return x
        
        # Square root of a number greater than 2 will
        # always fall between 2 and number/2.
        left = 2
        right = x // 2
        # So while our pointers don't meet
        while left <= right:
            # We'll just guess halfway between the 
            # two pointers
            
            pivot = left + (right - left) // 2
            num = pivot ** 2
            
            # If the guess is too high, we'll move the
            # right pointer to the midpoint - 1
            if num > x:
                right = pivot - 1
                
            # If the guess is too low, we'll move the
            # left pointer up.
            elif num < x:
                left = pivot + 1
            
            # If it happens to be the sqrt, return
            else: 
                return pivot
        return right