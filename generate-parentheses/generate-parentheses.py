class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtracker(opened, closed, res):
            if len(res) == 2*n:
                ans.append("".join(res))
                return
            
            if opened < n:
                res.append("(")
                
                backtracker(opened + 1, closed, res)
                
                res.pop()
                
            if closed < opened:
                res.append(")")
                
                backtracker(opened, closed + 1, res)
                
                res.pop()
                
        
        backtracker(0, 0, [])
        return ans