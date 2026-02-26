#19. REmove nth node form the end of a list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        fast=slow=head
        for i in range(n):
            fast=fast.next
        if not fast:
            return slow.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head