class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Start off at end
        i = len(nums) - 2
        
        # Find where the first instance of the decrease is
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        
        # If it exists (if it doesn't, i would be -1)
        if i >= 0:
            # Find out what to swap i with
            j = len(nums) - 1
            
            # Iterate backwards again until first number bigger than nums[i]
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            # Swap
            nums[i], nums[j] = nums[j], nums[i]
         
        # Reverse the rest of the array after i
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        