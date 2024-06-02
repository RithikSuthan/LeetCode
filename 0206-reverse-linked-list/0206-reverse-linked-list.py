# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import copy
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1=None
        temp=head
        while(temp):
            curr_next=temp.next
            temp.next=head1
            head1=temp
            temp=curr_next
        return head1
