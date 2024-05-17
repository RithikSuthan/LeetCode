# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ls=[]
        for i in range(len(lists)):
            temp=lists[i]
            while(temp):
                ls.append(temp.val)
                temp=temp.next
        
        ls.sort()
        head=None
        for i in ls:
            newNode=ListNode(i)
            if head==None:
                head=newNode
            else:
                temp=head
                while(temp.next):
                    temp=temp.next
                temp.next=newNode
        print(ls)
        return head
        