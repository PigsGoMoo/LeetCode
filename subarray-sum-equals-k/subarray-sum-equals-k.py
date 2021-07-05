class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Doesn't take negatives into consideration
#         # Sliding window
#         # Expand if <= k
#         # Retract if > k
#         left = right = 0
#         tot = nums[0]
#         ans = 0
        
#         while right < len(nums):
#             if tot == k:
#                 ans += 1
#             # Expand while less or equal
#             if tot <= k or left == right:
#                 right += 1
#                 if right == len(nums):
#                     break
#                 tot += nums[right]
                
#             elif tot > k and left < right:
#                 tot -= nums[left]
#                 left += 1
                    
#         return ans

#         # Simple brute force but takes too long in Python
#         ans = 0
#         for i in range(len(nums)):
#             tot = 0
#             for j in range(i, len(nums)):
#                 tot += nums[j]
#                 if tot == k:
#                     ans += 1
                    
#         return ans
        
        # Use a dictionary of running sums and a count of how many times it's come up
        # Then, as we iterate through, our current sum - k will be equal to whatever we need that might be in the dict
        # ex: imagine array [1, 2, 3, 4, -1] and k = 3
        # Our running sum array would be [0, 1, 3, 6, 10, 9]
        # So we can see that from 0 -> 3 is an increase of k. From 3 -> 6, and again from 6 -> 9
        # thus the answer should be 3
        
        count = 0
        sums = {
            0: 1,
        }
        tot = 0
        for num in nums:
            tot += num
            count += sums.get(tot - k, 0)
            sums[tot] = sums.get(tot, 0) + 1
            
        return count        
        