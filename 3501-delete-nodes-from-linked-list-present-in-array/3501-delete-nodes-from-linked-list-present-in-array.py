# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        st=set(nums)
        
        while head and head.val in st:
            head=head.next
        
        curr=head
        prev=head
        while curr:
            # print(curr.val)
            while curr and curr.val in st and curr.next:
                prev.next=curr.next
                curr=curr.next
            if curr.val in st and not curr.next:
                prev.next=None
            prev=curr
            curr=curr.next
        return head
