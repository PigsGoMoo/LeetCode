class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Use a stack to keep track of which function is currently running
        # Initialize the answer array at 0 for each func
        # When a new func starts, add the current running time for the current function 
        # before starting new one
        # When a function ends, add time from start to end to ans
        # Means we need to also keep track of a timestamp where something begins
        # Can use the stack to do that. It'll keep track of [funcID, begin_time]
        # When a function ends, we modify the start time of the one below the current stack
        # to the end time of the function that just ended
        
        ans = [0] * n
        stack = []
        
        # Iterate through the logs
        for x in logs:
            # Grab log - log[0] will be ID, [1] is start/end, [2] is timestamp
            log = x.split(':')
            func_id, process, timestamp = int(log[0]), log[1], int(log[2])
            # If this is a start log
            if process == 'start':
                # We need to add it to the stack
                # but first, we need to increment the previous time run for previous func
                if stack:
                    ans[stack[-1][0]] += (timestamp - stack[-1][1])
                # then we add on the stack
                stack.append([func_id, timestamp])
            # If it's an end time
            else:
                # We need to finalize the ans array with full run time
                ans[func_id] += (timestamp + 1 - stack[-1][1])
                # Then pop the func from stack
                stack.pop()
                # Then update the last item in stack's start time to current process end time
                # if applicable
                if stack:
                    stack[-1][1] = timestamp + 1
                    
        
        return ans
        