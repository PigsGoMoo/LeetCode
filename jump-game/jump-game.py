class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize variable to keep track of our jump
        current_jump = 0
        print(nums)
                
        # Loop through array
        for i in range(len(nums) - 1):
            # Check the next furthest jump
            current_jump = max(current_jump, i + nums[i])
            
            if i == current_jump and i != len(nums) - 1:
                return False
            
        return True