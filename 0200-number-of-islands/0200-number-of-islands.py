class Solution(object):
    def numIslands(self, grid):
        visit=set()
        directions=[
            [1,0],[-1,0],[0,-1],[0,1]
        ]
        islands=0
        def bfs(r,c,directions,grid):
            queue=[]
            queue.append((r,c))
            while(queue):
                # print(queue)
                curr=queue.pop()
                # print(curr)
                visit.add(curr)
                # print(visit)
                for i in directions:
                    u=curr[0]+i[0]
                    v=curr[1]+i[1]
                    if u>=0 and u<len(grid) and v>=0 and v<len(grid[0]) and (u,v) not in visit and grid[u][v] =='1':
                            queue.append((u,v))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1' and (row,col) not in visit:
                    bfs(row,col,directions,grid)
                    islands+=1
                # print("next call")
        return islands