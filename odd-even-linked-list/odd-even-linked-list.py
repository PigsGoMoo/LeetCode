# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = True
        
        curr_odd = oddList = ListNode()
        curr_even = evenList = ListNode()
        
        while head:
            if odd:
                curr_odd.next = head
                curr_odd = curr_odd.next
            else:
                curr_even.next = head
                curr_even = curr_even.next
                
            head = head.next
            odd = not odd
            
        curr_even.next = None
        curr_odd.next = evenList.next
        
        return oddList.next