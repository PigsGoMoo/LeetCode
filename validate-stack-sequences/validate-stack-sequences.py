class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Idea is that the first value in popped means you have to push everything before
        # that value. So we can navigate to the index of the first popped value in pushed and 
        # have a pointer there. Then we iterate through popped and make sure
        # that the change is no more than one index going left.
        # We're allowed to have multiple indexes skipped going right because
        # We'll just be pushing them in as we go. 
        # We will also need a map of indexes that we've already "popped" from the 
        # push array so that we can know which ones to not count when going left.
        
        # Find first value of popped in pushed
        push_ptr = 0
        popped_vals = set()
        
        # Iterate through popped
        for val in popped:
            # For each value, we need to make sure it's no more than one index left
            # Because they are all distinct values, we can be inefficient and use .index
            push_idx = pushed.index(val)
            
            # If the index of the current popped value is greater than the last one
            if push_idx > push_ptr:
                # It's valid. So set the push pointer to this index
                push_ptr = push_idx
            
            # If the index of current popped is less than
            elif push_idx < push_ptr:
                # We need to check and see that it's not more than one away
                # but have to bear in mind of ones we've already popped
                # Easiest in while loop until we hit the index
                while push_ptr > push_idx:
                    # Decrement the pointer by one
                    push_ptr -= 1
                    # If it's not in popped values and not equal to push_ptr, 
                    if push_ptr not in popped_vals and push_ptr != push_idx:
                        # Then it's not valid
                        return False
                    
                    # Otherwise, it'll either be in popped val and != idx
                    # or not be in popped val and == idx
                    # in which case we can just continue until while loop exits
            # Add this value to popped regardless of which if statement we went into    
            popped_vals.add(push_idx)
            
        return True
        