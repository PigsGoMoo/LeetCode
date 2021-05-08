# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         lmidpoint = rmidpoint = len(nums) // 2
#         res = ltree = rtree = TreeNode(nums[lmidpoint])
        
#         lmidpoint -= 1
#         while lmidpoint >= 0:
#             ltree.left = TreeNode(nums[lmidpoint])
#             ltree = ltree.left
#             lmidpoint -= 1
            
#         rmidpoint += 1
#         while rmidpoint < len(nums):
#             rtree.right = TreeNode(nums[rmidpoint])
#             rtree = rtree.right
#             rmidpoint += 1

        def treeMaker(left, right):
            if left > right:
                return None
            
            midpoint = (left + right) // 2
            
            root = TreeNode(nums[midpoint])
            root.left = treeMaker(left, midpoint - 1)
            root.right = treeMaker(midpoint + 1, right)
            return root
        
            
        return treeMaker(0, len(nums) - 1)