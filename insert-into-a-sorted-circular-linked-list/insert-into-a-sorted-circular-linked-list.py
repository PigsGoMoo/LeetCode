"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        ans = Node(insertVal)
        
        if not head:
            ans.next = ans
            return ans
        
        curr = head
        
        while curr:
            if curr.val <= insertVal < curr.next.val:
                ans.next = curr.next
                curr.next = ans
                return head
            
            elif curr.next.val < curr.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    ans.next = curr.next
                    curr.next = ans
                    return head
                
            elif curr.next.val == curr.val and curr.next == head:
                ans.next = curr.next
                curr.next = ans
                return head
            
            curr = curr.next