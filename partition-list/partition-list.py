# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Edge case
        if not head or not head.next:
            return head
        
        
        # Initialize new list to return
        # Iterate through original and if < x, remove node
        # Connect to original list
        
        ans = prev = ListNode()
        curr = head
        
        # If first node is < x
        if curr.val < x:
            # Connect to ans
            prev.next = curr
            prev = prev.next
            
            # Iterate until we find a node > x
            # Iterate the prev list to that spot, as well
            while curr.next.val < x:
                # head = head.next
                curr = curr.next
                prev = prev.next
                if not curr.next:
                    return ans.next

                
            # Initialize slow to first node larger than x
            # head = head.next
            curr = curr.next

            
        head = slow = curr
        # Move curr to next node
        curr = curr.next
        
        # Iterate through rest of nodes      
        while curr:
            # If < x
            if curr.val < x:
                # Remove node
                prev.next = curr
                slow.next = curr.next
                curr = curr.next
                prev = prev.next
            else:
                curr = curr.next
                slow = slow.next
                
        # At this point, all values lower than x should be removed
        # Just need to connect the two lists now
        prev.next = head
        
        return ans.next
        