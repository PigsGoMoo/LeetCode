# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        
        queue = []
        if not root:
            return ans
        
        node = root
        
        queue.append([node, 0])
        
        while queue:
            node, level = queue.pop(0)
            if level + 1 > len(ans):
                ans.append([node.val])
            else:
                ans[level].append(node.val)
            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
                
        return ans