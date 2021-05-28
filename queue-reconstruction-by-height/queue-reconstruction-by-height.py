class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Make a new list to be number of people taller, height, index
        # Sort. Now the list is sorted by number of people first and heights second
        order = [(front, height, idx) for idx, (height, front) in enumerate(people)]
        
        order.sort()
        ans = []
        
        for f, h, idx in order:
            # We'll skip if each of them have nothing higher in front 
            # because it's already in appropriate order
            if f == 0:
                ans.append(people[idx])
                # print("Adding {} to end of ans".format(people[idx]))
                continue
                
            # So then we just need to check each front value
            # For whatever the f value is, we move that far back
            # Eg: if f == 2, we'll move back until there are two values bigger 
            # and then until all the smaller values are covered.
            
            i = 0
            ptr = 0
            # Move until f values in front are higher
            while i < f and ptr < len(ans):
                if h <= ans[ptr][0]:
                    # print("Current height is less than current pointer in ans")
                    i += 1
                    
                ptr += 1
                # print("Pointer is at {}".format(ptr))
                
                
            # After exiting the while loop, search until all the lesser values are passed
            while ptr < len(ans) and ans[ptr][0] < h:
                # print("Lesser value detected, incrementing pointer")
                ptr += 1
                
            # When we exit that while loop, our pointer is where the current value should go
            if ptr >= len(ans):
                # print("Adding {} to end of ans".format(people[idx]))
                ans.append(people[idx])
            else:
                # print("Adding {} to index {} of ans".format(people[idx], ptr))
                ans.insert(ptr, people[idx])
            
            # print(ans)
            
        return ans
                