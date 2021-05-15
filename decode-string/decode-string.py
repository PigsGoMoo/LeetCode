class Solution:
    def decodeString(self, s: str) -> str:
        # We can use stacks to accomplish this
        # Add letters to the string stack
        # and numbers to the number stack
        # When we hit an open bracket, push it into stack
        # When we hit a close bracket, we pull out the last string and the number
        # And decode from there. Then continue
        
        # Initialize
        curr_string = ""
        curr_val = ""
        
        string_stack = []
        num_stack = []
        
        for char in s:
            # If it's a letter, put into string
            if char.isalpha():
                curr_string += char
                # print("Adding {} to {}".format(char, curr_string))
            
            # Add numbers into curr_Val
            elif char.isnumeric():
                curr_val += char
                # print("Adding {} to {}".format(char, curr_val))
            
            # If we hit an open bracket, append the curr string and value into respective stacks
            elif char == "[":
                string_stack.append(curr_string)
                num_stack.append(int(curr_val))
                # print("{} reached. Appending {} to {} and {} to {}".format(char, curr_string, string_stack, curr_val, num_stack))
                curr_string = ""
                curr_val = ""
            
            # If we hit a close bracket, we decode from the stack.
            else:
                # print("{} reached.".format(char, curr_string))
                num = num_stack.pop()
                ans = "" if not string_stack else string_stack.pop()
                # Add string to answer num times. 
                for _ in range(num):
                    # print("Adding {} to {}".format(string, ans))
                    ans += curr_string
                    
                curr_string = ans
                
        return "".join(string_stack) + curr_string
            
                