# Date: 29-01-2026
#92. Reverse Linked List II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        counter=1
        prev=None
        curr=head
        if left==right==1:
            return head
        if left-right==0:
            return head
        while counter<left:
            nextNode=curr.next
            prev=curr
            curr=nextNode
            counter+=1
        home=prev
        while counter>=left and counter<=right:
            nextNode=curr.next
            if prev==home:
                end=curr
            if prev!=home:
                curr.next=prev
            prev=curr
            curr=nextNode
            counter+=1
        if end.next:
            end.next=curr
        if left==1:
            return prev
        home.next=prev
        return head