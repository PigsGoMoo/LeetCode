# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        fast = slow = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                pointer1 = head
                while pointer1 != slow:
                    slow = slow.next
                    pointer1 = pointer1.next
                    
                return slow
                
        return None
        
        