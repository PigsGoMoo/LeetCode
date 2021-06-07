class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # We can make a graph to get us from one point to the other
        # The graph will map parent to child, with parent being the number in front
        # and child being the one after.
        # We'll keep track of the in degrees of each child. We'll reduce the indegree by one every time we use
        # the parent. If it hits 0, that's the next number in the list.
        # The list will be a queue of numbers that have an in degree of 0 after current parent is done
        # If there is more than one number in the list, that means there are multiple different
        # ways to permutate the next values, thus resulting in false
        
        # Initialize the graph
        graph = {}
        in_degree = {}
        
        for seq in seqs:
            for num in seq:
                graph[num] = []
                in_degree[num] = 0
        
        # Populate the graph
        for seq in seqs:
            for idx in range(len(seq) - 1):
                parent = seq[idx]
                child = seq[idx + 1]
                # Graph links parent to child
                graph[parent].append(child)
                # In degree keeps track of how many point to child
                in_degree[child] += 1
                
        # Edge cases
        # If not enough numbers. Constraints say that all numbers are unique 
        # so we won't have a problem with hash map key clashing
        if len(graph) != len(org):
            return False
                
        # Find first number
        order = []
        
        for key in in_degree:
            if in_degree[key] == 0:
                order.append(key)
                
        # Loop through and get final
        ans = []
        
        while order:
            # If there's multiple possible values at any given point in time, that means that we 
            # can have multiple permutations
            if len(order) > 1:
                return False
            
            val = order.pop()
            # If the next number in org is different than the one we're about to add
            if val != org[len(ans)]:
                return False
            
            # Otherwise, add value and find next to add to order list
            ans.append(val)
            # Find children
            for child in graph[val]:
                # Reduce in_degree of each child
                in_degree[child] -= 1
                # If none left, append
                if in_degree[child] == 0:
                    order.append(child)
        
        # Outside of our loop, we have made the order and checked if each value lines up properly inside the while loop
        # Now just return if lengths are the same (redundant at this point, but just in case)
        return len(ans) == len(org)