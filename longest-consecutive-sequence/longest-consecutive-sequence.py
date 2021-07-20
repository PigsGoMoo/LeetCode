import collections
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I feel like this is easier with UF
        # Connect the consecutive elements
        # At the end, navigate through each head and return the length of longest
        
        UF = {}
        
        if not nums:
            return 0
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
                
            return UF[x]
        
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            
            UF[find(x)] = find(y)
            
            
        seen = set()
        
        for num in nums:
            if num - 1 in seen:
                union(num, num - 1)
            if num + 1 in seen:
                union(num, num + 1)
            
            seen.add(num)
        
        ans = 1
        head_count = collections.defaultdict(int)
        for key in UF:
            head = find(key)
            head_count[head] += 1
            ans = max(ans, head_count[head])
            
        return ans
        