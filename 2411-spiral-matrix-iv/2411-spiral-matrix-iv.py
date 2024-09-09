# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans=[[0 for j in range(n)] for i in range(m)]
        curr=head
        cnt_row=0
        cnt_col=0

        if n == 1: 
            for i in range(m):
                if curr:
                    ans[i][0] = curr.val
                    curr = curr.next
                else:
                    ans[i][0] = -1
            return ans
        
        if m == 1:
            for i in range(n):
                if curr:
                    ans[0][i] = curr.val
                    curr = curr.next
                else:
                    ans[0][i] = -1
            return ans

        while(cnt_row<(m+1)//2 and cnt_col<(n+1)//2):
            row=cnt_row
            col=cnt_col
            # print("loop 1 col ",col," row ",row," cnt_row ",cnt_row," cnt_col ",cnt_col)
            while(col<n-cnt_col):
                if curr:
                    ans[row][col]=curr.val
                    curr=curr.next
                else:
                    ans[row][col]=-1
                col+=1
            col-=1
            row+=1
            # print(ans)
            # print("loop 2 col ",col," row ",row," cnt_row ",cnt_row," cnt_col ",cnt_col)
            while(row<m-cnt_row):
                if curr:
                    ans[row][col]=curr.val
                    curr=curr.next
                else:
                    ans[row][col]=-1
                row+=1
            row-=1
            col-=1
            # print(ans)
            # print("loop 3 col ",col," row ",row," cnt_row ",cnt_row," cnt_col ",cnt_col)
            while(row > cnt_row and col>=cnt_col):
                if curr:
                    ans[row][col]=curr.val
                    curr=curr.next
                else:
                    ans[row][col]=-1
                col-=1
            col+=1
            row-=1
            # print(ans)
            # print("loop 4 col ",col," row ",row," cnt_row ",cnt_row," cnt_col ",cnt_col)
            while(col < n - cnt_col and row>cnt_row):
                if curr:
                    ans[row][col]=curr.val
                    curr=curr.next
                else:
                    ans[row][col]=-1
                row-=1
            cnt_row+=1
            cnt_col+=1
        # print(ans)
        return ans