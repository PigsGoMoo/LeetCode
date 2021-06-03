class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Same strat as other max window question
        # Except this time we need to modify nums
        # Use deque to keep track of max
        # Purge deque every value
        
        deque = collections.deque()
        
        def helper(i):
            # Clear old values
            if deque and i >= k and deque[0] == nums[i-k]:
                deque.popleft()
                
            # Clear all smaller values from right
            while deque and nums[i] > deque[-1]:
                deque.pop()
                
            
        # Loop through nums
        for i in range(len(nums)):
            # Add highest value to nums
            nums[i] += deque[0] if deque else 0
            # Purge deque
            helper(i)
            # Append as next highest if not negative
            if nums[i] > 0:
                deque.append(nums[i])
            
        # Return
        return max(nums)            
            