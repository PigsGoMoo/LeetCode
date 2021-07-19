"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # So we want in-order dfs
        # And convert from there
        # root.left.next = root
        # root.next = root.right
        # root.right.next = root.parent
        
        inorder = []
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            inorder.append(root)
            dfs(root.right)
            
        
        dfs(root)
        for idx, node in enumerate(inorder):
            if idx == 0 and len(inorder) > 1:
                node.right = inorder[1]
                node.left = inorder[-1]
            elif idx == len(inorder) - 1:
                node.right = inorder[0]
                node.left = inorder[idx - 1]
            else:
                node.right = inorder[idx + 1]
                node.left = inorder[idx - 1]
                
        return inorder[0] if inorder else root       
        