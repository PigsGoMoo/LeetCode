# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # In a post-order traversal of the tree, the root node is the very last node you see. 
        # So we can use postorder[-1] to determine root
        # Then we can use in-order to determine which side is left and which is right because
        # in-order goes from left to root to right. So inorder.index(postorder[-1]) is the
        # index of the root. Anything less than that is on the left branch. Anything to the right
        # is in the right branch.
        # Can recursively call and repeat this process to make the tree
        
        def helper(inorder_l, inorder_r):
            # Return empty subtree
            if inorder_l > inorder_r:
                return None
            
            # Last element of postorder is root
            val = postorder.pop()
            root = TreeNode(val)
            
            # Root splits the inorder list between left and right subtrees
            idx = idx_map[val]
            
            # Build the right subtree
            # Build right first because we're going backwards from postorder
            # and postorder is left -> right -> root, so we go root -> right -> left
            # Build recursively.
            root.right = helper(idx + 1, inorder_r)
            
            # Build left subtree
            root.left = helper(inorder_l, idx - 1)
            
            return root
        
        # Build the index map of inorder traversal to reference
        idx_map = {val : idx for idx, val in enumerate(inorder)}
        
        # Invoke + return ans
        return helper(0, len(inorder) - 1)