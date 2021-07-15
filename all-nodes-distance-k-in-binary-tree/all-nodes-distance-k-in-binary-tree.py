# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Append a parent to each node and then use BFS outward like in Dijkstra
        def append_parent(node, parent = None):
            if node:
                node.par = parent
                append_parent(node.left, node)
                append_parent(node.right, node)
                
        
        append_parent(root)
        
        # Start our BFS at the target with distance 0
        q = collections.deque([(target, 0)])
        visited = {target}
        
        while q:
            # If the next result is distance k away, that means we're done
            # Remember that in order to get to distance k, we have to go through all distance k-1
            # and add their neighbors to the queueueueueue. Once we hit the first one at k distance away,
            # that means we've finished all the k-1 distances, so this list is now complete.
            if q[0][1] == k:
                return [node.val for node, dist in q]
            
            # Otherwise, BFS. Add all neighbors not yet visited to queueueuuee
            node, dist = q.popleft()
            for nei in [node.left, node.right, node.par]:
                if nei and nei not in visited:
                    visited.add(nei)
                    q.append((nei, dist + 1))
        
        # Only reaches this point if never reach k distance away
        return []
