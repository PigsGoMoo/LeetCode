class Solution:
    def numWays(self, n: int, k: int) -> int:
        # The number of ways to paint n fences with k colors with these constraints is
        # based on the previous amounts
        # If there's only one fence, you can only do k options
        # If there's two fences, you can do k * k (because you can use any color up to two times, we're not
        # constrained, so it's all possibilities twice)
        # After the second fence, the third one can either be the same color, in which case it's the same ans
        # as before (multiplied by one color) 
        # or different, in which case it's the same answer as before multiplied by k-1 different colors
        # The final answer for n posts is the same + different of the previous. As such, we can use dynamic programming
        # to build the answers from the bottom up
        if n == 1:
            return k
        
        same = k
        
        diff = k * (k - 1)
        
        for i in range(2, n):
            same, diff = diff, (same + diff) * (k - 1)
            
        return same + diff
        