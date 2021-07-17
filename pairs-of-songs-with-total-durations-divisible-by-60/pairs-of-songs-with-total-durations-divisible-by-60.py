class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # We keep a list of remainders
        # If we meet a number with a remainder of 20, then any number with a remainder 40
        # will work. 
        # If we meet a number with remainder 0, then we need another with remainder 0 to work
        remainders = collections.defaultdict(list)
        ans = 0
        
        for val in time:
            remain = val % 60
            
            if remain == 0:
                need = 0
            else:
                need = 60 - remain
                
            if need in remainders:
                ans += len(remainders[need])
                
            remainders[remain].append(val)
            
        return ans
        