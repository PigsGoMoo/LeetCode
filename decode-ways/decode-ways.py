from functools import lru_cache
class Solution:
    
    @lru_cache(maxsize=None)
    def recurse(self, idx, s):
        
        # Base case
        # If past end of string
        if idx == len(s):
            return 1
        
        # If value is 0, can't be decoded
        if s[idx] == '0':
            return 0
        
        # If end of string. Needs to be checked after 0 in case of input '0'
        if idx == len(s) - 1:
            return 1
        
        # Recurse with next index
        ans = self.recurse(idx + 1, s)
        # Check if valid two number
        if int(s[idx: idx+2]) <= 26:
            # If so, add and recurse after two more spots
            ans += self.recurse(idx + 2, s)
            
        return ans        
        
    
    def numDecodings(self, s: str) -> int:
        # Top down recursion with memoization
        
        return self.recurse(0, s)