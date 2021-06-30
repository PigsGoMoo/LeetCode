class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # A graph is bipartite if you can essentially alternate it
        # For example, first node is 1, second node is 2, third node is 1, fourth is 2, etc
        # Also - every neighboring node to the first one has to be a 2
        # and every node of that neighbor has to be 1
        # We can use a hash to keep track of which value each node is.
        # If we hit a node with the wrong value, return False
        values = {}
        
        for i in range(len(graph)):
            # If we haven't visited this node yet
            if i not in values:
                # Initialize stack to keep track of all the neighbors + traversal order
                stack = [i]
                # Set value of this node to 0
                values[i] = 0
                # Iterate through
                while stack:
                    # Grab next node in stack
                    node = stack.pop()
                    # Iterate through neighbors
                    for neighbor in graph[node]:
                        # If not yet visited
                        if neighbor not in values:
                            # Add to stack
                            stack.append(neighbor)
                            # Set its value to opposite of our current value
                            values[neighbor] = values[node] ^ 1
                        # If it's already visited and its value is equal to current one
                        elif values[neighbor] == values[node]:
                            return False
        
        return True
        