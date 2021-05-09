# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        self.count = 0
        self.unival(root)
        return self.count
        
        
    def unival(self, node):
            
        if not node.left and not node.right:
            self.count += 1
            return True
        
        is_uni = True
        
        if node.left:
            is_uni = self.unival(node.left) and is_uni and node.left.val == node.val
            
        if node.right:
            is_uni = self.unival(node.right) and is_uni and node.right.val == node.val
            
        self.count += is_uni
        return is_uni
        
            