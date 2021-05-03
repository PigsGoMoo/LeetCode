class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Default dict makes it so when you make a key, there will be a "default" value pair for it already
        # Useful if you want your value pair to be an array but don't want to have to initialize the array
        # first.
        ans = collections.defaultdict(list)
        
        for s in strs:
            ans[tuple(sorted(s))].append(s)
            
        return ans.values()