# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp=head
        ls=[]
        while(temp):
            ls.append(temp.val)
            temp=temp.next
        # print(ls)
        # if x not in ls:
        #     ls.sort(key=lambda x:x)
        small=[]
        big=[]
        for i in range(0,len(ls)):
            if ls[i]>=x:
                big.append(ls[i])
            else:
                small.append(ls[i])
        small.extend(big)
        temp=head
        for i in range(0,len(small)):
            temp.val=small[i]
            temp=temp.next
        return head
        