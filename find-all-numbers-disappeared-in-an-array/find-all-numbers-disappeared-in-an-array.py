class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Works but too slow
#         ans = [i for i in range(1, len(nums) + 1)]
        
#         for num in set(nums):
#             ans.remove(num)
            
#         return ans

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
                
        ans = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                # We have to append i + 1 because original nums go from 1 -> n, not 0 -> n. 
                # When we make it negative, we subtract one. So when we check, we need to add 1 back.
                ans.append(i + 1)
                
        return ans