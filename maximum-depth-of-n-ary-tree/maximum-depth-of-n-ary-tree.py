"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
#         if not root:
#             return 0
        
#         depth = 0
#         def dfs(node, level):
            
#             nonlocal depth
            
#             depth = max(level, depth)
            
#             if not node:
#                 return
            
#             for child in node.children:
#                 dfs(child, level + 1)
                
#             return
        
#         dfs(root, 1)
        
#         return depth
        if not root:
            return 0
        
        if not root.children:
            return 1
        
        height = [self.maxDepth(child) for child in root.children]
        
        return max(height) + 1