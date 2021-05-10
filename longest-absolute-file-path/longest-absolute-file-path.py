class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        # Initialize variables
        ans = 0
        table = {-1: 0}
        
        # Split up lines
        for line in input.split('\n'):
            # Count how deep into subdirectory you are. Depth = amount of tabs
            depth = line.count('\t')
            
            if line.count('.'):
                ans = max(table[depth - 1] + len(line), ans)
            else:
                table[depth] = table[depth - 1] + len(line) - depth
                
        return ans
                