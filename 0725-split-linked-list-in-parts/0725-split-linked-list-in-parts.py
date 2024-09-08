# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ls=[]
        temp=head
        while temp:
            ls.append(temp.val)
            temp=temp.next
        l1=len(ls)
        if l1==0:
            return [None for i in range(k)]
        print(ls)
        ans=[]
        if k>=l1:
            curr=head
            for i in range(k):
                if i<l1:
                    temp=curr.next
                    curr.next=None
                    ans.append(curr)
                    curr=temp
                else:
                    ans.append(None)
        else:
            ind=[0 for i in range(k)]
            temp_l1=l1
            start=0
            while temp_l1!=0:
                ind[start]+=1
                start+=1
                if start>=len(ind):
                    start=0
                temp_l1-=1
            print(ind)
            curr=head
            start=0
            end=l1
            cou=0
            while(start<end and cou<len(ind)):
                temp_end=start+ind[cou]
                temp_prev=None
                temp_start_node=curr
                while(start<temp_end):
                    temp_prev=curr
                    curr=curr.next
                    start+=1
                temp_prev.next=None
                ans.append(temp_start_node)
                cou+=1
        return ans