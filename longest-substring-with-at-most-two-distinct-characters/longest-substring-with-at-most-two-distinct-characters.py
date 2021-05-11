class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Initialize window + tracker and ans to return
        seen = {}
        ans = 0
        left = right = 0
        
        # Increase window size
        while right < len(s):
            char = s[right]
            
            # Add char to window
            seen[char] = seen.get(char, 0) + 1
            
            # If window too big
            # Contract window until only two left
            while left < right and len(seen) > 2:
                char = s[left]
                    
                seen[char] -= 1
                if seen[char] == 0: 
                    del seen[char]
                    
                left += 1
            
            ans = max(ans, right - left + 1)

            right += 1
            
        return ans