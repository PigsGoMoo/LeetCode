class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Work from right to left
        # Keep track of highest in a stack
        # if we reach something higher, get rid of all values lower in that stack and replace it with higher value
        # If we reach something lower, add it to the stack
        # Also keep track of indexes
        ans = [0] * len(temperatures)
        
        stack = []
        n = len(temperatures)
        
        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            if stack:
                ptr = len(stack) - 1
                while ptr >= 0:
                    if temp < stack[ptr][0]:
                        ans[i] = stack[ptr][1] - i
                        stack.append((temp, i))
                        break
                    elif temp >= stack[ptr][0]:
                        stack.pop()
                        if not stack:
                            stack.append((temp, i))
                    
                    ptr -= 1
                
            else:
                stack.append((temp, i))
            
        return ans
        