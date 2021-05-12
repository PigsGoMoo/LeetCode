# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
#         #  Method can add the nodes up, but doesn't give you the best results in cases where your "best" path
#         #  is one where the it doesn't traverse a path or doesn't traverse a complete path.
#         # Ex: [1, -2, 3] -> ans is 4 because best path is from 1 -> 3, ignoring -2. 
#         node_sums = []
        
#         def postOrder(node):
#             if node.left:
#                 postOrder(node.left)
                
#             if node.right:
#                 postOrder(node.right)
                
#             if not node.left and not node.right:
#                 node_sums.append(node.val)
#             else:
#                 l = node.left.val if node.left else 0
#                 r = node.right.val if node.right else 0
#                 node.val = max(node.val + l + r, node.val)
#                 node_sums.append(node.val)
                
#         postOrder(root)
#         return max(node_sums)

        # First off, we need to take into consideration that the entire tree isn't a valid path
        # You'd only be able to traverse down one side of the tree because we can't travel back up a node once we
        # go down it.
        # So we need to make it so that the max value of a node is just a max of one of the nodes + curr node
        
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Max sum on left and right sides of the node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Price to start new path at current node
            new_path = node.val + left_gain + right_gain
            
            # Update max_sum if this path is better
            max_sum = max(max_sum, new_path)
            
            # For recursion purposes, return max gain if we continue on the same path
            return node.val + max(left_gain, right_gain)
        
        max_sum = float('-inf')
        max_gain(root)
        return max_sum