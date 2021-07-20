class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # [7, 1, 13, 18, 4], k = 6
        # [1, 2, 3, 3, 1]
        # If there's multiple of one type of remainder in the cumulative sum divided by k, then there's an answer
        # As seen above, 1 appears twice so then the subarray from 2 to the next 1 is the answer
        # This is because the difference in the two cumulative sums from the second 1 to the first 1 is a multiple of 6
        # 7 % 6 = 1
        # So anything whose cumulative sum % 6 == 1 after will mean the subarray is a multiple of 6
        # ex: 37 % 6 = 1, so 37 - 7 must be divisible by 6
        # Because in order to get from the first number to the second with the same remainder, we'd have to add
        # a multiple of 6 to do so.
        # But because we need a subarray of size 2 minimum, we also need to make sure the repeated remainder
        # isn't within one index
        # ex: [7, 12, 3, 5, 10]
        # %6: [1, 1, 4, 3, 1] -- the first instance of the double 1 won't work because it would mean 12 alone is 
        # the "subarray" but it's invalid cuz size < 2. 3, 5, 10 are valid because it's a size of 3
        
        # We need to initialize the remainder of 0 so that if the cumulative sum ever equals a multiple, we 
        # can just return it
        seen = {0: -1}
        
        curr = 0
        for idx, num in enumerate(nums):
            curr += num
            if idx - seen.setdefault(curr % k, idx) > 1:
                return True
            
        return False
        