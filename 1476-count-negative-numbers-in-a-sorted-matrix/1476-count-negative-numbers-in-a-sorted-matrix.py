class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0
        for i in range(rows):
            grid[i].sort()
            left=0
            right=cols
            while(left<right):
                mid=(left+right)//2
                print(left,mid,right)
                if grid[i][mid]>=0:
                    right=mid
                else:
                    left=mid+1
            count+=right
            print("Iteration ",i,count)
        print(count)
        return count