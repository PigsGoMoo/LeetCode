class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         [2, 2, 2, -3, -3]
#         [1, 1, -1]
        # DP solution? Make an array of differences between cost - gas for each index
        # If that array sum is <= 0, then it's possible. If >= 1, then we cannot.
        # Start would be at first negative index?
        # [2, 2, -3, 2, -3] would start at 2?
        # [1, 2, 3, 4, 5] - gas
        # [3, 4, 0, 6, 2] - cost
        
        # dp = [c - g for c, g in zip(cost, gas)]
        dp = []
        tot = 0
        for idx, (c, g) in enumerate(zip(cost, gas)):
            val = c - g
            dp.append(val)
            tot += val
        
        # print(dp, tot, first)
        if tot > 0:
            return -1
        else:
            # [-1, 3, -1, 2, -3]
            # Keep sum. If > 0, reset. Keep track of first neg
            # If hit end of array and sum <= 0, return first neg
            valid = 0
            reset = True
            last_neg = 0
            for idx, num in enumerate(dp):
                if num < 0 and reset:
                    valid += num
                    reset = False
                    last_neg = idx
                else:
                    valid += num
                    
                if valid > 0:
                    reset = True
                    valid = 0
                    
            return last_neg
        