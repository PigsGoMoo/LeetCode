# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        # Initialize variables
        curr = head
        length = 0
        
        # Determine length of linked list
        while curr:
            length += 1
            curr = curr.next
            
        if not length or length == 1:
            return head
        
        # The number of rotations we need is actually just the remainder of the k divided by number of nodes
        rotations = k % length
        
        # Edge cases
        if rotations == 0:
            return head
        
        
        # Initialize nodes to iterate through + answer node
        prev = ListNode()
        curr = head
        
        # Iterate through the list until we're at our starting point. Starting point is at position rotations - 1 from
        # the end of the list
        for i in range(length - rotations):
            # We need to detach the end node from the start of the first node to prevent circular lists
            if i == length - rotations - 1:
                end = curr
            curr = curr.next
            
        end.next = None
        
        # Link answer to start
        prev.next = curr
        
        # Iterate through. Once we hit the end of the original list, link it back to the head
        for i in range(length):
            # Make sure to not link if we're at the end node
            if not curr.next and i != length - 1:
                curr.next = head
            
            curr = curr.next
            
                
        return prev.next