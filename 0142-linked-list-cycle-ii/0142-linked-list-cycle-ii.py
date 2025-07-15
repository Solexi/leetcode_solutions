# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = []
        if not head:
            return None
        
        while head and head.next:
            if head in visited_nodes:
                return head
            visited_nodes.append(head)
            head = head.next
        return None
        # if not head:
        #     return "no cycle"
        # slow = head
        # fast = head.next

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         entry = head
        #         while entry != slow:
        #             entry = entry.next
        #             slow = slow.next
        #         return entry
        # return "no cycle"

        