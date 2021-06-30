"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        ans = Node(node.val)
        
        if node in self.visited:
            return self.visited[node]
        
        self.visited[node] = ans
        
        for neighbor in node.neighbors:
                ans.neighbors.append(self.cloneGraph(neighbor))
                        
        return ans