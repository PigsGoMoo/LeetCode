class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Initialize possible values
        candidates = [i for i in range(1, 10)]
        
        # Initialize answer array
        ans = []
        
        # Edge case
        if n > 45:
            return ans
        
        # Make backtracker function
        def backtracker(k, target, combos, candidates):
            # Base case - if target reached and combo found
            if k == 0 and target == 0:
                ans.append(combos[:])
            # Base case - current sum greater than n or no more candidates
            elif k == 0 or sum(combos) > n or not candidates:
                return
            
            # Base case - remaining values to choose from are higher than remaining target
            elif candidates[0] > target:
                return
            
            # Base case - remaining values to choose from never reach target
            elif sum(candidates) < target:
                return 
            
            # Loop through candidates
            for i in range(len(candidates)):
                # Add one candidate
                combos.append(candidates[i])
                # Backtrack
                backtracker(k - 1, target - candidates[i], combos, candidates[i+1:])
                # Pop
                combos.pop()
                
        
        backtracker(k, n, [], candidates)
        return ans