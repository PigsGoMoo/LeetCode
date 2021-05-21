# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # Recurse through tree. If we need to remove it, set children nodes as roots and add to ans
        
        # Make to_delete a set for more efficient lookup
        to_delete_set = set(to_delete)
        
        # Initialize
        ans = []
        
        # Make helper func for recursion
        def helper(root, is_root):
            # Base case
            if not root:
                return None
            
            # Set variable to boolean value of whether or not to delete
            deleted = root.val in to_delete_set
            
            # If this is a root value (aka if parent was deleted) and this one isn't deleted
            if is_root and not deleted:
                # Add to ans
                ans.append(root)
                
            # Recurse left
            # delete will tell whether or not the next one is root or not.
            # because if this node is deleted, the children will be new roots. 
            root.left = helper(root.left, deleted)
            # Recurse right
            root.right = helper(root.right, deleted)
            
            # Return node if not deleted
            return None if deleted else root
        
        
        # Invoke helper
        helper(root, True)
        
        return ans