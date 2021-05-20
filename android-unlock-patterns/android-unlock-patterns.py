class Solution:
    
    def __init__(self):
        # We'll make our map of variables that are skipped
        # We access it by using self.skip[x][y] where x and y are the numbers we're connecting.
        self.skip = [[0] * 10 for _ in range(10)]
        
        # Now set the values
        self.skip[1][3] = self.skip[3][1] = 2
        self.skip[3][9] = self.skip[9][3] = 6
        self.skip[7][9] = self.skip[9][7] = 8
        self.skip[1][7] = self.skip[7][1] = 4
        self.skip[1][9] = self.skip[9][1] = self.skip[3][7] = self.skip[7][3] = self.skip[2][8] = \
        self.skip[8][2] = self.skip[4][6] = self.skip[6][4] = 5
        
        # Initialize visited
        self.visited = set()
        self.visited.add(0)
        
        
    def make_pattern(self, start, remain):
        # Base cases
        if remain < 0:
            return 0
        
        elif remain == 0:
            return 1
        # Add to visited
        self.visited.add(start)
        
        ans = 0
        
        # Loop through and add all possible numbers to combo
        for i in range(10):
            # If we haven't added that number yet and we've visted the cross value
            if i not in self.visited and self.skip[start][i] in self.visited:
                # Call recursively
                ans += self.make_pattern(i, remain - 1)
                
        # Remove from visited after looping through all possible values
        self.visited.remove(start)
        # Return 
        return ans
        
        
    def numberOfPatterns(self, m: int, n: int) -> int:
        # Brute force way is to backtrack every solution
        # But then we need to find a way to keep track of the jumps that are not allowed
        # We can map out the numbers that are skipped
        # Another possible optimization is that the patterns for 1,3,7,9 are all the same - just rotated 90 degrees
        # Same with 2, 4, 6, 8. So we can just find one and multiply by 4 for both of those
        # And then do one last search starting at 5
        
        ans = 0
        
        # Search through each length character
        for i in range(m - 1, n):
            # 1, 3, 7, 9 are symmetrical, so we just need to figure out the ans for 1 and multiply by 4
            ans += self.make_pattern(1, i) * 4
            # 2, 4, 6, 8 also symmetrical
            ans += self.make_pattern(2, i) * 4
            # Lastly, solve for 5
            ans += self.make_pattern(5, i)
            
            
        return ans
