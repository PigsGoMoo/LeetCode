# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # We'll use a stack to keep track of values 
        # Then make our ans LL from back to front
        l1_stack = []
        l2_stack = []
        
        ptr = l1
        while ptr:
            l1_stack.append(ptr.val)
            ptr = ptr.next
        
        ptr = l2
        while ptr:
            l2_stack.append(ptr.val)
            ptr = ptr.next
            
        ans = None
        carry = 0
        while l1_stack or l2_stack:
            a = l1_stack.pop() if l1_stack else 0
            b = l2_stack.pop() if l2_stack else 0
            
            val = a + b + carry
            carry = 0
            if val >= 10:
                val -= 10
                carry += 1
                
            temp = ListNode(val, ans)
            ans = temp
            
        if carry:
            temp = ListNode(1, ans)
            ans = temp
            
        return ans
        