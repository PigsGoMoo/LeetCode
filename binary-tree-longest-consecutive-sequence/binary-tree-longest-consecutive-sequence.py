# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        # Increasing is only on the right
        # So we continually check the right side as we traverse the tree 
        # and keep track of longest from there
        # Probably easier with recursion.
        
        longest = 0
        
        def dfs(node, length = 1):
            
            nonlocal longest 
            
            longest = max(longest, length)
            
            if node.left:
                if node.left.val == node.val + 1:
                    dfs(node.left, length + 1)
                else:
                    dfs(node.left)
                
            if node.right:
                if node.right.val == node.val + 1:
                    dfs(node.right, length + 1)
                else:
                    dfs(node.right)
                
            return
        
        
        dfs(root)
        return longest