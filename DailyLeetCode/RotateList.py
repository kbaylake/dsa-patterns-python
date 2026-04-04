
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        slow=fast=head
        cnt=1
        for i in range(k):
            if fast.next:
                fast=fast.next
                cnt+=1
            else:
                k=k%cnt
                if k==0:
                    return head
                fast=head
                for j in range(k):
                    fast=fast.next
                break
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        newHead=slow.next
        slow.next=None
        fast.next=head
        return newHead