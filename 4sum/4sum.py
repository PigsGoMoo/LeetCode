class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Sort the input array
        nums.sort()
        
        # kSum helper function
        def kSum(nums, target, k):
            # Initialize results array
            res = []
            
            # If the sum of the first k numbers is too big
            # or the sum of the last k numbers is too small
            # We'll never be able to hit the target, so return nothing.
            if sum(nums[:k]) > target or sum(nums[-k:]) < target or len(nums) == 0:
                return res
            
            # When we only have twoSum left, run the twoSum helper function
            if k == 2:
                return twoSum(nums, target)
        
            # For each run in the kSum, we run through the values of nums, starting the loop
            # one index later each time for each value of k until k == 2
            # and then we add the results to the results array and return it. 
            # At the end of the for loop in the first call of the kSum function (aka once all the recursion is done)
            # we'll have all of our possible results.
            for i in range(len(nums)):
                # Skip any repeated numbers
                if i == 0 or nums[i-1] != nums[i]:
                    temp = kSum(nums[i+1:], target - nums[i], k-1)
                    for answer in temp:
                        res.append([nums[i]] + answer)
            
            return res
        
        # When k == 2, we run twoSum
        def twoSum(nums, target):
            # Standard 2 sum function
            res = []
            left, right = 0, len(nums) - 1
            
            while left < right:
                total = nums[left] + nums[right]
                
                # We check for duplicates in the or and skip it
                if total < target or (left > 0 and nums[left] == nums[left-1]):
                    left += 1
                    
                elif total > target or (right < len(nums) - 1 and nums[right] == nums[right+1]):
                    right -= 1
                
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
            return res
        
        
        
        return kSum(nums, target, 4)
        