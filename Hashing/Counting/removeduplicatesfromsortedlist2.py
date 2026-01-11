class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        op=ListNode(0,head)
        prev=op
        slow=head   
        fast=head.next
        if not fast.next:
            if slow.val==fast.val:
                return None
            else:
                return head
        while fast:
            if slow.val==fast.val:
                while slow.val==fast.val:
                    fast=fast.next
                    if not slow or not fast:
                        prev.next=fast
                        return op.next
                prev.next=fast
            else:
                prev=slow
            slow=fast
            fast=fast.next
        return op.next 