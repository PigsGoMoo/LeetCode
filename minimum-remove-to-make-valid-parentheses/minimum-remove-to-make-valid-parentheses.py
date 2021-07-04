class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # We can make a stack to keep track of valid ones
        # Anything left in stack after end gets removed
        # Add every '(' to stack and remove it when we hit ')'
        # If we hit a ')' and nothing in stack, add it to be removed
        
        # Stack will keep track of the parenthesis, so we know which can be removed at the end
        # Remove will keep track of how many of each to be removed. Need to keep track of index
        stack = []
        remove = []
        
        # Iterate through string
        for idx, char in enumerate(s):
            # If it's an open, we add to stack
            if char == '(':
                stack.append((char, idx))
            # If it's closed, we either remove from stack or add to remove cuz no opening
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove.append(idx)
            # Do nothing if letter
            
        # Add whatever is left of stack to remove
        for i in range(len(stack)):
            remove.append(stack[i][1])
            
        remove.sort()
        ptr = 0
        ans = ''
        
        for idx, char in enumerate(s):
            if ptr < len(remove) and idx == remove[ptr]:
                ptr += 1
                continue
            
            ans += char
            
        return ans
                