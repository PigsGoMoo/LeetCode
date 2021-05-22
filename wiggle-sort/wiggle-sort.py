class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We should just be able to swap as we go down the line
        # If next number is bigger when it should be smaller, swap it
        up = True
        
        for i in range(len(nums) - 1):
            if up:
                # i + 1 value should be greater than i value here
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                
            else:
                # i + 1 value should be less than i value here
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    
            up = not up
            
            