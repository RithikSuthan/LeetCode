class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for j in range(n)] for i in range(n)]
        curr=1
        cnt_row=0
        cnt_col=0

        while(cnt_row<(n+1)//2 and cnt_col<(n+1)//2):
            row=cnt_row
            col=cnt_col
            while(col<n-cnt_col):
                ans[row][col]=curr
                curr+=1
                col+=1
            col-=1
            row+=1
            while(row<n-cnt_row):
                ans[row][col]=curr
                curr+=1
                row+=1
            row-=1
            col-=1
            while(row > cnt_row and col>=cnt_col):
                ans[row][col]=curr
                curr+=1
                col-=1
            col+=1
            row-=1
            while(col < n - cnt_col and row>cnt_row):
                ans[row][col]=curr
                curr+=1
                row-=1
            cnt_row+=1
            cnt_col+=1
        return ans
