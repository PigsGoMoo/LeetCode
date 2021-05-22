# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Initialize
        diameter = 0
        
        # Helper func to recursively go through each node
        def longest_path(node):
            # Base case
            if not node: 
                return 0
            # Call the variable that stores highest
            nonlocal diameter
            
            # Recursively find longest path from right and left sides
            left = longest_path(node.left)
            right = longest_path(node.right)
            
            # Update diameter, if larger found
            diameter = max(diameter, left + right)
            
            # Return the longer path + 1 to include parent node
            return max(left, right) + 1
        
        
        # Invoke + return
        longest_path(root)
        return diameter