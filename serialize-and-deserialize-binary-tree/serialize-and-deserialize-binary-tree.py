# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # It's just traverse the tree however and turn result into a string
        def recurse(root, s):
            if not root:
                s += 'None,'
            else:
                s += str(root.val) + ','
                s = recurse(root.left, s)
                s = recurse(root.right, s)
                
            return s
        
        return recurse(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # To deserialize, just make the tree the way we traversed it. In our case, we did preorder dfs
        def unrecurse(q):
            # We'll use a queueue to do this
            
            if q[0] == 'None':
                q.popleft()
                return None
            
            root = TreeNode(q[0])
            q.popleft()
            root.left = unrecurse(q)
            root.right = unrecurse(q)
            return root
        
        arr = data.split(',')
        q = collections.deque([x for x in arr])
        root = unrecurse(q)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))