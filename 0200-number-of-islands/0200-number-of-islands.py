class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        no_of_islands=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visited=set()
        rows=len(grid)
        cols=len(grid[0])

        def dfs(i,j):
            print((i,j))
            if (i,j) in visited:
                return
            visited.add((i,j))
            for x,y in directions:
                u=i+x
                v=j+y
                if u in range(0,rows) and v in range(0,cols) and grid[u][v]=="1" and (u,v) not in visited:
                    dfs(u,v)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    no_of_islands+=1
        return no_of_islands