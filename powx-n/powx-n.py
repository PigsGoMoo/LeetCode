class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def helper(x, n):
            
            if x == 0 or x == 1:
                return x
        
            if n == 0:
                return 1
        
            if n == 1: 
                return x
            
            half = helper(x, n//2)
            
            if n % 2 == 0:
                return half * half
            else:
                return half*half*x

        if n < 0:
            n = -n
            x = 1/x
            
            
        return helper(x, n)
        
        