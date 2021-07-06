class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        nums = []
        alpha = []
        
        for word in logs:
            arr = word.split()
            if arr[1].isnumeric():
                nums.append(word)
            else:
                alpha.append(word)
                
        alpha.sort(key= lambda x: (x.split(" ", maxsplit=1)[1], x.split()[0]))
        
        return alpha + nums
    