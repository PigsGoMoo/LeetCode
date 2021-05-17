"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        stack = [root]
        ans = []
        
        while stack:
            level = []
            res = []
            for node in stack:
                level.extend(node.children)
                res.append(node.val)
                
            ans.append(res)
            stack = level
            
        return ans