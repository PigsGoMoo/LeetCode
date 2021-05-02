class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        ans = []
        
        def backtracker(nums, target, combo):
            
            if target == 0:
                if combo not in ans:
                    ans.append(combo[:])
                    
            if target < 0:
                return
            
            for i in range(len(nums)):
                combo.append(nums[i])
                
                backtracker(nums[i + 1:], target - nums[i], combo)
                
                combo.pop()
                
        if min(candidates) > target:
            return ans
        
        if sum(candidates) < target:
            return ans
            
        backtracker(candidates, target, [])
        
        return ans