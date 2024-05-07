# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        stack=[]
        while(temp):
            while stack and stack[-1].val<temp.val:
                stack.pop()
            stack.append(temp)
            temp=temp.next

        # print(stack)
        # for i in range(len(stack)-1):
        #     stack[i].next=stack[i+1]
        # stack[-1].next=None
        # return stack[0]
        nxt = None
        while stack:
            cur = stack.pop()
            cur.next = nxt
            nxt = cur
        
        return cur