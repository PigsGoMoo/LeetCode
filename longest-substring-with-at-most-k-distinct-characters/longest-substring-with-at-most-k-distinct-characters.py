class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Idea is to use a sliding window to keep track of longest
        # If we hit a letter that gives us k+1 characters in our window, 
        # We'll retract the window until there are k characters again.

        
        # Initialize
        n = len(s)
        window = {}
        ans = 0
        left = right = 0
        
        # Edge cases
        if k == 0:
            return 0
        
        if n == 1:
            return 1
        
        window[s[right]] = window.get(s[right], 0) + 1
        
        # Iterate through the string
        while right + 1 < n:
            # Expand the window
            right += 1
            # Add value to window
            window[s[right]] = window.get(s[right], 0) + 1
            
            # If window size > k, start retracting window
            if len(window) > k:
                # Stop retracting when window size == k again
                while left < right and len(window) > k:
                    # Remove char from window
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                    # Retract window
                    left += 1
                    
            
            # Update ans if applicable
            ans = max(ans, right - left + 1)
        
            
        return ans
        