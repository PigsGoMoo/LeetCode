class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        carry1 = 1
        # Based on how we multiply normally. 32 * 26 = 6 * 2 + 6 * 30 + 20 * 2 + 20 * 30
        # Or: (6 * 2) + (6 * 3 * 10) + (2 * 10 * 2) + (2 * 10 * 3 * 10)
        for i in num1[::-1]:
            
            carry2 = 1
            
            for j in num2[::-1]:
            
                res += int(i) * int(j) * carry1 * carry2
                carry2 *= 10
                
            carry1 *= 10
            
        return str(res)