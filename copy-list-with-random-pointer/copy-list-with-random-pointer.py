"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        arr = {}
        ans = prev = Node(0)
        curr = head
        
        # Iterate through list, making new nodes as you go
        while curr:
            # Make new node
            node = Node(curr.val)
            # Connect to previous node
            ans.next = node
            # Iterate to new node
            ans = ans.next
            # Add node to arr
            arr[curr] = node
            
            # Iterate curr
            curr = curr.next
        
        curr = head
        ans = prev.next
        
        while curr:
            idx = curr.random
            if idx:
                ans.random = arr[idx]
            else:
                ans.random = None
            
            curr = curr.next
            ans = ans.next
        
        return prev.next
            