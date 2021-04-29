class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                count += 1
                
            elif num == 0:
                count = 0
                
            if count > maxCount:
                maxCount = count
                
        return maxCount