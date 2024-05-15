class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows=len(grid)
        cols=len(grid)
        ans=[]
        for i in range(rows-2):
            val=[]
            for j in range(cols-2):
                temp_max=float("-inf")
                for x in range(3):
                    for y in range(3):
                        print(grid[x+i][y+j],end=" ")
                        temp_max=max(temp_max,grid[x+i][y+j])
                val.append(temp_max)
            ans.append(val)
        print(ans)
        return ans

