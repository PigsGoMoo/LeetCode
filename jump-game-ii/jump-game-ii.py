class Solution:
    def jump(self, nums: List[int]) -> int:
        # Works but too slow because backtracking is 2^n      
#         min_jumps = [float('inf')]
        
#         def backtracker(nums, jumps):
            
#             if len(nums) == 1:
#                 min_jumps[0] = min(jumps, min_jumps[0])
                
#             if not nums:
#                 return
            
#             for i in range(1, nums[0] + 1):
                
#                 backtracker(nums[i:], jumps + 1)
                
        
#         backtracker(nums, 0)
#         return min_jumps[0]

        # There is a way to do it with one pass. If we mark the "furthest" we can jump at any point
        # And keep track of that furthest jump, we can see how many jumps we'll need as we iterate through
        
        # Initialize variables. We need to keep track of how many jumps, the end of the current jump, and 
        # the next furthest jump from there
        jumps = 0
        current_jump_end = 0
        furthest_jump = 0
        
        for i in range(len(nums) - 1):
            # Each iteration, we see what the furthest we can get is with the values in the array
            furthest_jump = max(furthest_jump, i + nums[i])
            
            # Once we hit the end of our current jump, we make a new jump based on the furthest we found prior.
            # Then we reset current jump end and repeat until at end of array - 1 (because end of array isn't a jump)
            if i == current_jump_end:
                jumps += 1
                current_jump_end = furthest_jump
                
        return jumps
        