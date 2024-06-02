# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans=None
        carry=0
        while(l1 and l2):
            val=l1.val+l2.val+carry
            if val>9:
                carry=val//10
                val=val%10
            else:
                carry=0
            if ans==None:
                ans=ListNode(val)
            else:
                temp=ans
                while(temp.next):
                    temp=temp.next
                temp.next=ListNode(val)

            l1=l1.next
            l2=l2.next

        while(l1):
            temp=ans
            while(temp.next):
                temp=temp.next
            val=l1.val+carry
            if val>9:
                carry=val//10
                val=val%10
            else:
                carry=0
            temp.next=ListNode(val)
            l1=l1.next
        
        while(l2):
            temp=ans
            while(temp.next):
                temp=temp.next
            val=l2.val+carry
            if val>9:
                carry=val//10
                val=val%10
            else:
                carry=0
            temp.next=ListNode(carry)
            temp.next=ListNode(val)
            l2=l2.next

        if carry!=0:
            temp=ans
            while(temp.next):
                temp=temp.next
            temp.next=ListNode(carry)

        return ans