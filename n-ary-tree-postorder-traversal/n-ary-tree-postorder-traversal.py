"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Can cheat and do pre-order reversed
        stack = []
        ans = []
        
        if not root:
            return ans
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children)
                
        
        return ans[::-1]