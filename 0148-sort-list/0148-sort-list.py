# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]
        temp=head
        while(temp):
            ls.append(temp.val)
            temp=temp.next
        # print(ls)
        ls.sort()
        temp=head
        cou=0
        while(temp):
            temp.val=ls[cou]
            temp=temp.next
            cou=cou+1
        return head