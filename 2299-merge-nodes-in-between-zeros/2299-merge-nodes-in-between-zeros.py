# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        ls=[]
        sum1=0
        while (temp):
            if temp.val==0:
                if sum1!=0:
                    ls.append(sum1)
                sum1=0
            sum1+=temp.val
            temp=temp.next
        if sum1!=0:
            ls.append(sum1)
        # print(ls)
        temp=head
        cou=0
        while(temp and cou<len(ls)):
            temp.val=ls[cou]
            cou+=1
            if cou>=len(ls):
                break
            temp=temp.next
        temp.next=None
        return head
