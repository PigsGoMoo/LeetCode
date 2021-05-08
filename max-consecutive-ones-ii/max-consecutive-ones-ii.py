class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
#         if len(nums) == 1:
#             return 1
        
        
#         maxCount = 0
        
#         i = 0
#         print("New testcase: {}".format(nums))
        
#         while i < len(nums):
#             print(nums[i])
#             if nums[i] == 1:
                
#                 j = i
#                 count = 0
#                 flipped = False
#                 while j < len(nums):
#                     print("Inside inner while: {}".format(nums[j]))
#                     if nums[j] == 1:
#                         count += 1
#                         j += 1
#                     else:
#                         if not flipped:
#                             flipped = True
#                             i = j
#                             count += 1
#                             j += 1
#                         else:
#                             maxCount = max(maxCount, count)
#                             print("New max: {}".format(maxCount))
#                             break
                
#                 if not flipped:
#                     i = j
#                 maxCount = max(maxCount, count)
#                 print("New max: {}".format(maxCount))
            
#             i += 1
            
#         return maxCount

        # Initialize variables
        maxCount = 0
        left = right = 0
        num_zeroes = 0
        
        # Loop through array
        while right < len(nums):
            # Add on the next element. If it's a zero, add to zero count
            if nums[right] == 0:
                num_zeroes += 1
            
            # If zero count hits 2 (thus making it invalid)
            while num_zeroes == 2:
                # Move left up until only one zero in window
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1
            # Update maxCount each iteration
            maxCount = max(maxCount, right - left + 1)
            right += 1
            
        return maxCount