"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        ans = Node(None, None, head, None)
        
        def flatten_child(prev, curr):
            if not curr:
                return prev
            
            curr.prev = prev
            prev.next = curr
            
            tempNext = curr.next
            
            tail = flatten_child(curr, curr.child)
            
            curr.child = None
            
            return flatten_child(tail, tempNext)
        
        
        flatten_child(ans, head)
        
        ans.next.prev = None
        return ans.next