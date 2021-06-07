class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Sliding window - let's keep track of max dif by keeping track
        # of min and max values in the window
        # If dif isn't greater than limit, we keep extending.
        # If it is, we slide the window to the right, not retracting 
        # (aka limit changed).
        
        # Initialize
        left = right = 0
        min_val = float('inf')
        max_val = float('-inf')
        counter = {}
        ans = 0
        
        # Loop through
        while right < len(nums):
            # Start by adding value to window 
            min_val = min(min_val, nums[right])
            max_val = max(nums[right], max_val)
            # print("Left: {}, Right: {}, min: {}, max: {}, window: {}".format(left, right, min_val, max_val, nums[left:right + 1]) )
            counter[nums[right]] = counter.get(nums[right], 0) + 1
            # print("Counter: {}".format(counter))
            # Compare to limit
            diff = max_val - min_val
            # print("Diff: {}, limit: {}".format(diff, limit))
            # If less or equal, extend
            if diff <= limit:
                ans = max(ans, right - left + 1)
                # print("Still works. Saving {}".format(ans))
                right += 1
                
            # If it's greater, retract right window and slide window to the right, removing left from window
            else:
                # At this point, right is one higher than it should be, so we need to subtract 1
                ans = max(ans, right - left)
                # print("Saving {} to ans".format(ans))
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                    
                counter[nums[right]] -= 1
                if min_val == nums[left]:
                    min_val = min(counter)
                if max_val == nums[left]:
                    max_val = max(counter)
                left += 1
        # print(right, left)
        # Don't need to do right - left + 1 because right will be one after the end already, which is the +1 we need
        return ans
                    
            