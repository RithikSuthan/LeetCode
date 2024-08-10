class Solution:
    from collections import deque
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows=len(grid)
        newGrid=[[0 for j in range(rows*3)] for i in range(rows*3)]
        for i in range(rows):
            for j in range(rows):
                baserow=i*3
                basecol=j*3
                if grid[i][j]=="/":
                    newGrid[baserow][basecol+2]=1
                    newGrid[baserow+1][basecol+1]=1
                    newGrid[baserow+2][basecol]=1
                elif grid[i][j] == "\\": 
                    newGrid[baserow][basecol]=1
                    newGrid[baserow+1][basecol+1]=1
                    newGrid[baserow+2][basecol+2]=1
        # print(newGrid)
        visited=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(v1,v2):
            visited.add((v1,v2))
            for i in directions:
                u=v1+i[0]
                v=v2+i[1]
                if u in range(0,len(newGrid)) and v in range(0,len(newGrid[0])) and (u,v) not in visited and newGrid[u][v] !=1:
                    bfs(u,v)
        div=0
        for i in range(0,len(newGrid)):
            for j in range(0,len(newGrid[0])):
                if newGrid[i][j]!=1 and (i,j) not in visited:
                    # print("Call for ",(i,j))
                    bfs(i,j)
                    div+=1
                    # print(visited)
        return div
