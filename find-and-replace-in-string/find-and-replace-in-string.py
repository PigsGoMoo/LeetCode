class Solution:
    def findReplaceString(self, s: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        
        # Edge cases
        if not s or not targets: 
            return s
        
#         # We can solve this and keep the integrity of the indexes by working from right to left.
#         grouped = []

#         Group values together with index first so we can sort them in backwards order
#         for i in range(len(targets)):
#             idx = indexes[i]
#             source = sources[i]
#             target = targets[i]
#             grouped.append((idx, source, target))
            
#         grouped.sort(reverse = True)

#         Loop through and replace if criterion is met
#         for idx, source, target in grouped:
#             if s[idx: idx + len(source)] == source:
#                 s = s[:idx] + target + s[idx + len(source):]

            
#         return s
    
        # Can be condensed
        for idx, source, target in sorted(zip(indexes, sources, targets), reverse = True):
            s = s[:idx] + target + s[idx + len(source):] if s[idx : idx+len(source)] == source else s
            
        return s
        