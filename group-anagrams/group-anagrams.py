class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Default dict makes it so when you make a key, there will be a "default" value pair for it already
        # Useful if you want your value pair to be an array but don't want to have to initialize the array
        # first.
#         ans = collections.defaultdict(list)
        
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
            
#         return ans.values()
        ans = collections.defaultdict(list)
    
    
        def getKey(counter):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            res = ""
            for letter in alphabet:
                res += 'letter{}'.format(counter.get(letter, 0))
                
            return res
        
        
        for s in strs:
            counter = {}
            
            for char in s:
                counter[char] = counter.get(char, 0) + 1
            
            key = getKey(counter)
            
            ans[key].append(s)
            
        return ans.values()