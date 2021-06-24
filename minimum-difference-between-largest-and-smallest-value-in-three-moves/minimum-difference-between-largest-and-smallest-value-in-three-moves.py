class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        # Edge cases
        if len(nums) <= 4:
            return 0
        
        # Since the difference is determined by largest - smallest values, we just need to change those
        # With 3 moves, we have 4 possible options
        # Change 3 largest values
        # Change 2 largest values + 1 smallest
        # Change 1 largest values + 2 smallest
        # Change 3 smallest
        # Answer will be the smallest of these 4 possibilities
        
        nums.sort()
        min_diff = float('inf')
        
        for i in range(4):
            diff = nums[-4 + i] - nums[i]
            if diff == 0:
                return 0
            min_diff = min(min_diff, diff)
            
        return min_diff