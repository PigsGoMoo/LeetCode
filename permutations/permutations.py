class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtracker(nums, path):
            # print("Backtracker called with nums {} and path {}".format(nums, path))
            
            if len(nums) == 1:
                path.append(nums[0])
                # print("Only one value in nums. Adding to path {} and appending to answer".format(path))
                ans.append(path[:])
                path.pop()
                return
            
            for i in range(len(nums)):
                path.append(nums[i])
                # print("{} appended to path {}".format(nums[i], path))
                removed = nums.pop(i)
                # print("{} removed from nums: {}. Calling backtracker with path {}".format(removed, nums, path))
                backtracker(nums, path)
                
                path.pop()
                nums.insert(i, removed)
                # print("Popping path back to {} and resetting nums back to {}".format(path, nums))
                
                
        backtracker(nums, [])
        return ans