# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]
        temp=head
        while(temp):
            ls.append(temp.val)
            temp=temp.next
        
        i=0  #Inserion sort
        j=len(ls)
        while(i<j):
            val=min(ls[i:j+1])
            ind=ls[i:j+1].index(min(ls[i:j+1]))+i
            ls.pop(ind)
            ls.insert(i,val)
            i=i+1

        temp=head
        cou=0
        while(temp):
            temp.val=ls[cou]
            temp=temp.next
            cou=cou+1
        return head
        