# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        start = head
        while start is not None:
            length += 1
            start = start.next
        
        if length == n:
            return head.next
        
        start = head
        for i in range(length - n -1):
        # for i in range(1, n+1):
            start = start.next
            
        start.next = start.next.next
        
        return head
        
        
            
        