# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        stack = []
        
        if not root:
            return ans
        
        node = root
        
        def postOrder(node):
            if node.left:
                postOrder(node.left)
            if node.right:
                postOrder(node.right)
                
            ans.append(node.val)
            
        postOrder(node)
        # Iterative approach not yet finished
#         while node or stack:
#             while node:
#                 stack.append(node)
#                 node = node.left
                
#             node = stack.pop()
#             ans.append(node)
#             node = node.right
            
        return ans