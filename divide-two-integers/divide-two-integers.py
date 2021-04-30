class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        # This method is brute force and too slow
#         if divisor == 1:
#             return dividend
        
#         if divisor == -1:
#             return dividend * -1

#         count = 0
#         if dividend < 0:
#             numerator = -1
#             dividend *= -1
#         else:
#             numerator = 1
            
#         if divisor < 0:
#             denominator = -1
#             divisor *= -1
#         else:
#             denominator = 1
            
#         while dividend > 0:
#             dividend -= divisor
#             count += 1
            
#         if dividend < 0:
#             count -= 1
            
#         return count * numerator * denominator

        # Here, instead of trying to subtract, we try to see how many times it goes in
        count = 0
        
        # We work with negatives because it's 32-bit and there are more negatives than positives.
        # Helps resolve overflow possibility if we try to do abs(-2**31) 
        # because positive only goes to 2*31 - 1 and negatives goes to -(2**31) (aka one more number)
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
            
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        # Initialize our loop. Once divisor is bigger, we know we can't subtract anymore
        # Remember that because we're dealing with negatives, all signs are flipped from what they'd normally be
        while dividend <= divisor:
            # This keeps track of how many times we double the divisor
            doubler = -1
            value = divisor
            
            # Double the current value and make sure it's less than the remaining dividend.
            # Second part of while loop prevents overflow
            while value + value >= dividend and value >= -(2**31) // 2:
                value += value
                doubler += doubler
                
            # Once we exit, we know that doubling value again will make it higher than dividend.
            # So we add this to the current answer and repeat until we can't anymore
            count += doubler
            # And subtract from dividend
            dividend -= value
            
        # Return count once you exit the loop
        return count if negatives == 1 else -count