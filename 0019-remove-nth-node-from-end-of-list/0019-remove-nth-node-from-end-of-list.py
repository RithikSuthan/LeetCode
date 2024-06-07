# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cou=0
        temp=head
        while(temp):
            cou+=1
            temp=temp.next
        if cou==n:
            head=head.next
            return head
        temp=head
        while(temp and cou-1>n):
            temp=temp.next
            cou=cou-1
        print(temp.val)
        if temp and temp.next:
            if temp.next.next!=None:
                temp.next=temp.next.next
            else:
                temp.next=None
            return head
        return None