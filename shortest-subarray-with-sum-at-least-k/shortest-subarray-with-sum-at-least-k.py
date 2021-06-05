class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
#         left = right = tot = 0
        
#         min_size = float('inf')
        
#         while right < len(nums):
#             print("Left: {}, Right: {}".format(left, right))
#             # Add new number
#             tot += nums[right]
#             print("Total: {}".format(tot))
#             # If >= k
#             while tot >= k or nums[left] <= 0:
#                 # Record size
#                 if tot >= k:
#                     min_size = min(min_size, right - left + 1)
#                 if min_size == 1:
#                     return 1
#                 # Retract window
#                 tot -= nums[left]
#                 left += 1
                
#             # Extend window
#             right += 1
            
#         return min_size if min_size != float('inf') else -1
        # Use a deque to keep track of idx and current sum up to that index
        # Compare it with the current sum up to that index
        # If current sum up to current index - current sum up to deque index >= k
        # Then we have a possible answer. Record it then pop it from deque because
        # It's the first occurrence of an answer for that index (thus shortest)
        # As we go, we also need to make sure the deque is always increasing, too
        # Meaning if the current sum is less than the sums at the end of the deque, 
        # We pop those out and add this new one. We do this because if the sum at the
        # end of the deque is bigger, that means our difference (remember, we're comparing the
        # difference, which is our k) is smaller. So a smaller current sum means bigger difference
        # and also since those haven't found any matches to make it greater than k yet,
        # it will also result in a shorter answer
        
        # Items in deque will be our left pointer, essentially
        deque = collections.deque([[0,0]])
        # Curr will be the total sum up to current index
        curr = 0
        ans = float('inf')
        # print("We're dealing with array: {} and k: {}".format(nums, k))
        # And this is our right pointer
        for i in range(len(nums)):
            # Add value to total sum
            curr += nums[i]
            # print("i: {}, current sum up to this point: {}".format(i, curr))
            # Compare with first value
            while deque and curr - deque[0][1] >= k:
                # print("Possible answer: {}, idx: {}".format(deque[0], deque[0][0]))
                ans = min(ans, i + 1 - deque.popleft()[0])
                # print("Ans is now: {}".format(ans))
                
            # If current total sum is less than values at end, we can remove them
            # Because this will result in higher differences between curr and deque as well 
            # as shorter windows
            while deque and curr <= deque[-1][1]:
                # print("Latest curr is less than {}, so we pop.".format(deque[-1][1]))
                deque.pop()
                
            # print("Adding new index to deque")
            deque.append([i + 1, curr])
            
        return ans if ans != float('inf') else -1
        