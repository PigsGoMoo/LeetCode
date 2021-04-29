class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def fibHelper(n):
            
            if n in memo:
                return memo[n]
            
            if n == 0:
                return 0
            
            if n == 1:
                return 1
            
            memo[n] = fibHelper(n-1) + fibHelper(n-2)
            return memo[n]
        
        
        return fibHelper(n)