# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS but switch between a queueuueue and stack
        # Start out left to right
        # then switch r -> l
        q = collections.deque([root])
        stack = []
        reverse = False
        ans = []
        
        if not root:
            return ans
        
        while q or stack:
            level = []
            # q goes left
            if q:
                while q:
                    node = q.popleft()
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                    level.append(node.val)
            else:
                while stack:
                    node = stack.pop()
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                    level.append(node.val)
            ans.append(level)
            
            
        return ans
        