class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        
        def backtracker(nums, target, path):
            
            # print("Backtracker called with target {} and path {}".format(target, path))
            
            if target == 0:
                app = sorted(path)
                if app not in ans:
                    # print("Adding {} to ans cuz target is {}".format(app, target))
                    ans.append(app[:])
                return
            
            if target < 0:
                # print("Went over target. Going back...")
                return
            
            if min(nums) > target:
                # print("all values in nums greater than target. Skipping this round")
                return
            
            for num in nums:
                path.append(num)
                
                # print("Appending {} to {}. Calling backtracker with new target: {}".format(num, path, target - num))
                
                backtracker(nums, target - num, path)
                
                path.pop()
                
                # print("Removing {} from path: {}".format(num, path))
                
            
        if min(candidates) > target:
            return ans
        
        backtracker(candidates, target, [])
        
        return ans
            