class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Use a stack to keep track of number of characters in a row
        # If last item in stack == k, pop it and remove the letters from string
        # Then combine the stack. If the previous letter in stack == next letter in string, combine those
        # If 3 again, remove and repeat. If not, continue iterating
        # We can use two pointers to make this in one pass. 
        # If we need to remove characters, just move pointer back k spaces and overwrite from there
        
        stack = []
        arr = [c for c in s]
        
        fast = slow = 0
        
        while fast < len(arr):
            
            # Copy fast to slow
            arr[slow] = arr[fast]
            
            # Add char at fast to stack with current count
            # If last item same as current letter, just increment it
            if stack and stack[-1][0] == arr[fast]:
                stack[-1][1] += 1
            # If not same, append new item
            else:
                stack.append([arr[fast], 1])
                
            # Check if count == k
            if stack[-1][1] == k:
                # Remove it
                stack.pop()
                # Move slow back k spaces
                slow -= k
            
            # Increment pointers
            slow += 1
            fast += 1
            
        return ''.join(arr[:slow])
    