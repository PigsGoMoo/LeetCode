class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Get rid of the dashes and make everything upper case
        combined = "".join(s.split('-')).upper()
        
        ans = ""
        
        i = len(combined) - 1
        j = 0
        while i >= 0:
            j = (j + 1) % k
            ans = combined[i] + ans
            if not j and i != 0:
                ans = "-" + ans
            
            i -= 1
            
        return ans
