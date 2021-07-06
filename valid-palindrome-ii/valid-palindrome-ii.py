class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Standard two-pointer
        # Since there's only one possible dropped char, if we hit a mismatch, we can
        # just drop from left or right and continue rest of comparison
        left = 0
        right = len(s) - 1
        
        def helper(left, right, s):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
                
            return True
        
        
        while left < right:
            if s[left] != s[right]:
                return helper(left + 1, right, s) or helper(left, right - 1, s)
            
            left += 1
            right -= 1
            
        return True