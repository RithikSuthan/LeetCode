class Solution:
    from heapq import heappush,heappop
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        pq=[(0,0,0)]
        visited=[[False]*cols for i in range(rows)]
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        while pq:
            curr,i,j=heappop(pq)
            
            if visited[i][j]:
                continue
            visited[i][j]=True
            if i==rows-1 and j==cols-1:
                return curr
            for u,v in directions:
                x=u+i
                y=v+j
                if x in range(0,rows) and y in range(0,cols) and not visited[x][y]:
                    if grid[x][y]<=curr+1:
                        heappush(pq,(curr+1,x,y))
                    else:
                        wait_time=grid[x][y]-curr
                        if(wait_time%2==1):
                            heappush(pq,(grid[x][y],x,y))
                        else:
                            heappush(pq,(grid[x][y]+1,x,y))

        return -1