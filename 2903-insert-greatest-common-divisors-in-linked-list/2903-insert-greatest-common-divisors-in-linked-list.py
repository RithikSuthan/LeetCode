# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            result=min(a,b)
            while result:
                if a%result==0 and b%result==0:
                    break
                else:
                    result-=1
            # print(a,b," Gcd ",result)
            return result
        ls=[]
        curr=head
        while(curr):
            ls.append(curr.val)
            curr=curr.next
        gcd_ls=[]
        for i in range(0,len(ls)-1):
            gcd_ls.append(gcd(ls[i],ls[i+1]))
        final=[]
        for i in range(0,len(gcd_ls)):
            final.append(ls.pop(0))
            final.append(gcd_ls.pop(0))
        final.append(ls.pop(0))
        # print(gcd_ls)
        print(final)
        head1=None
        for i in final:
            if not head1:
                head1=ListNode(i)
            else:
                curr=head1
                while curr.next:
                    curr=curr.next
                curr.next=ListNode(i)
        return head1