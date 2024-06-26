# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]
        temp=head
        while(temp):
            if temp in ls:
                return temp
            else:
                ls.append(temp)
            temp=temp.next
        return None