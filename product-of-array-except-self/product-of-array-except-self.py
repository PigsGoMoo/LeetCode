class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Make two arrays - one is running product of all items from right and one from left til last element (exclusive)
        # Answer is the product of those two arrays at index i
        # Eg: nums = [1, 2, 3, 4]
        # right = [ 1,  1,  2, 6] Start off with 1, then right[0] * nums[0], etc...right[n-2] * nums[n-2]
        # left =  [24, 12,  4, 1] Start off with 1 on right side and do the same
        # Alternatively, we can start with entire product (right[n-1] * nums[n-1]) and divide (but question says we can't)
        
        n = len(nums)
        
        right = [1] * n
        left = [1] * n
        
        for i in range(1, n):
            right[i] = right[i - 1] * nums[i - 1]
            left[-i - 1] = left[-i] * nums[-i]
        
        return [x*y for x, y in zip(left, right)]
        