class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Needs refinement because there can be duplicate letters in t
        # Would need to have a count in the dictionary for each occurrence in t
        # Then check when count is 0 to determine whether or not we've hit all the letters
        # Edge cases
        # If both length of 1, just compare outright
        if len(t) == 1 or len(s) == 1:
            return t if t in s else ""
        
        # If t longer than s, it can't be found in s
        if len(t) > len(s):
            return ""
        
#         # Convert all to upper case for consistency
#         s.upper()
#         t.upper()
        
#         # Initialize variables
#         left = right = 0
#         tracker = {}
#         ans = ""
        
#         # Add initial value to tracker if it's one we're looking for
#         # The value pair for this will be [count, index]
#         # We'll use count to make sure that we've hit all we need and index to keep track of the position
#         # of the latest one
#         if s[0] in t:
#             tracker[s[0]] = 0
            
#         # Loop through string
#         while right < len(s) - 1:
#             right += 1
#             # If this is one of our letters
#             if s[right] in t:
#                 tracker[s[right]] = right
#                 # If it's already in the tracker
#                 # We can move the left window up to the next occurence if it's the same as the left idx
#                 if s[left] == s[right]:
#                     # Find next index
#                     left = min(tracker.values())
                                
#             # If we've found all the letters
#             if len(tracker) == len(t):
#                 if not ans:
#                     ans = s[left:right + 1]
#                 else:
#                     if right - left + 1 < len(ans):
#                         ans = s[left:right + 1]
            
#         return ans
        # Optimization: We can filter out all characters in s that is not in t, keeping track of indexes
        # Then we can do sliding window from there
        
        # Initialize variables
        tracker = {}
        filtered_s = []
        ans = ""
        
        # Initialize tracker with each letter in t
        for char in t:
            tracker[char] = tracker.get(char, 0) + 1
            
        for idx, char in enumerate(s):
            if char in tracker:
                filtered_s.append([idx, char])
                
        left = right = 0
        
        seen = {}
        
        numbers = len(tracker)
        windowed = 0
        
        while right < len(filtered_s):
            char = filtered_s[right][1]
            seen[char] = seen.get(char, 0) + 1
            if seen[char] == tracker[char]:
                windowed += 1
                
            while left < right and windowed == numbers:
                char = filtered_s[left][1]
                
                end = filtered_s[right][0]
                start = filtered_s[left][0]
                
                if end - start + 1 < len(ans) or not ans:
                    ans = s[start:end+1]
                    
                seen[char] -= 1
                if seen[char] < tracker[char]:
                    windowed -= 1
                
                left += 1
                
            right += 1
            
        return ans
                       
            