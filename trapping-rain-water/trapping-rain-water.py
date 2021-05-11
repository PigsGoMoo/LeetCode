class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0
        
        # Edge case
        if not height:
            return ans
        
        # Idea is to go left and keep a map of the max heights from left side
        # and repeat with map of max heights from right side
        # The minimum of the two is the one we use to calculate our answer
        
        n = len(height)
        
        # Initialize left_max with first value in height
        left_max = [height[0]] * n
        # Initialize right_max with last value in height
        right_max = [height[-1]] * n
        
        # Iterate once going left
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # Again going right
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Now compare and add to ans.
        for i in range(n):
            val = min(left_max[i], right_max[i])
            ans += val - height[i]
            
        return ans