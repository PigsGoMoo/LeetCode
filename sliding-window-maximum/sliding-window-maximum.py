class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Idea is to use deques. We'll keep the index of the max value in the deque
        # At each iteration of the window, we'll add the new value to the deque after purging
        # the one that leaves the window as well as any values less than the current
        # starting from the right end. This is because those elements won't be able to 
        # be the max. 
        # At every step, our max value will be at the 0th index of the deque every time.
        
        # Initialize
        n = len(nums)
        ans = []
        deque = collections.deque()
        # max_idx = 0
        
        # Helper func to purge the deque
        def helper(i):
            # First, purge all values outside the window
            if deque and deque[0] == i - k:
                deque.popleft()
                
            # Now remove all values in deque from end if they're lower than the
            # next value that we just added
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
                
        
        # Edge cases
        if n * k == 0:
            return ans
        
        if k == 1:
            return nums
        
        # Start the deque off with the first k values
        for i in range(k):
            helper(i)
            deque.append(i)
        
        # Add the max of the first window to ans    
        ans.append(nums[deque[0]])
        
        # Slide window and repeat steps
        for i in range(k, n):
            helper(i)
            deque.append(i)
            ans.append(nums[deque[0]])
        
        # Return ans
        return ans
        