class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        # Helper func to insert combo values in the middle of the dest values
        def insert(combo, dest):
            # Initialize
            res = []
            # Since we always use the last even number, we can just use floor division
            mid = len(dest[0]) // 2
            for num in combo:
                for val in dest:
                    res.append(val[:mid] + num + val[mid:])
            
            return res
        
        
        odd = ["0", "1", "8"]
        even = ["11", "69", "88", "96", "00"]
        
        ans = [[], odd, even[:4]]
        
        if n < 3:
            return ans[n]
        
        # Work bottoms up
        for i in range(3, n + 1):
            # if odd, we just add the odd ones in the middle of the last even one
            if i % 2:
                res = insert(odd, ans[i-1])
                
            else:
                res = insert(even, ans[i-2])
            
            ans.append(res)
            
        return ans[n]
    
    