class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def type(s):
            ans = ""
            
            for idx, char in enumerate(s):
                if char == '#':
                    if ans:
                        ans = ans[:len(ans)-1]
                else:
                    ans += char
            return ans
        
        return type(s) == type(t)