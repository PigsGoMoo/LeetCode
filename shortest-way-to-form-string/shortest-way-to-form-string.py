class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # We can map the source by index then have a pointer for that source
        # We'll increment pointer to the next occurrence of the character as we
        # traverse the target string
        # Every time we have to reset the pointer (current pointer is > last source map value)
        # we increment ans
        
        # Initialize
        ans = 1
        
        # Helper func to find the next position of the pointer if in middle
        def find_pointer(char, curr):
            arr = char_map[char]
            for idx in arr:
                if curr <= idx:
                    return idx + 1
            
        
        # Edge cases
        
        
        # Map characters
        char_map = collections.defaultdict(list)
        
        for idx, char in enumerate(source):
            char_map[char].append(idx)
            
        ptr = 0
        # Loop through target string
        for char in target:
            # For each character, we'll move the pointer to the next occurrence of that char
            # Edge case
            if char not in char_map:
                return -1
            # If current pointer location is past every available number
            if ptr > char_map[char][-1]:
                # Increase ans, reset pointer to first index + 1
                ans += 1
                ptr = char_map[char][0] + 1
            # If not
            else:
                # We need to find the next occurrence
                # Fastest is binary search?
                ptr = find_pointer(char, ptr)
                
        return ans if ans != 0 else -1
                
                
                