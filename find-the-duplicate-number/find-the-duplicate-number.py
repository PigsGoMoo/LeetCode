class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            
        # If they want constant extra space, use the fast + slow method to detect cycle like linked list