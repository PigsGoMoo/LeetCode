# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If we traverse by dfs, when we reach either p or q, we can bubble a True up
        # When we reach the other, the first time True comes from both sides (or from one side
        # and itself), that means that we're at the LCA
        
        def dfs(root):
            if not root:
                return False
            
            # Go left
            left = dfs(root.left)
            
            # Go right
            right = dfs(root.right)
            
            # Check self
            # Will be set to True if this node is either p or q
            node = root == p or root == q
            
            if node + left + right >= 2:
                self.ans = root
                
            return node or left or right
        
        
        dfs(root)
        return self.ans
        