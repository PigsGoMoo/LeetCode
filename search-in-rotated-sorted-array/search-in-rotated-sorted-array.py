class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute force method - O(n) time
        # for i in range(len(nums)):
            # if nums[i] == target:
                # return i
            
        # return -1
        
        # Binary search is O(log(n)) time
        
        # Edge case
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        # Find the pivot point
        
        left = 0
        right = len(nums) - 1 
        
        # If first number smaller than last number, that means there was no rotation (or rotated at 0)
        if nums[left] < nums[right]:
            mid = 0
            
        else:
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] > nums[mid + 1]:
                    mid += 1
                    break

                if nums[mid] >= nums[0]:
                    # Work on right of mid
                    left = mid+1

                else:
                    # Work on left of mid
                    right = mid - 1
                
        if nums[mid] == target:
            return mid
        
        print("Pivot found at index: {}".format(mid))
        
        if mid == 0:
            left = 0
            right = len(nums) - 1
        elif target > nums[0]:
            left = 0
            right = mid - 1
        elif target < nums[0]:
            left = mid
            right = len(nums) - 1
        else:
            return 0
        print("Searching for {} in between indexes {} and {} of array {}".format(target, left, right, nums))
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
                
        return -1