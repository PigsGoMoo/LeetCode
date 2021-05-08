class Solution:
    def thirdMax(self, nums: List[int]) -> int:
#         ans = sorted(list(set(nums)))

#         if len(ans) >= 3:
#             return ans[-3]
#         else:
#             return ans[-1]
        
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
                
        if len(maximums) == 3:
            return min(maximums)
        
        else:
            return max(maximums)