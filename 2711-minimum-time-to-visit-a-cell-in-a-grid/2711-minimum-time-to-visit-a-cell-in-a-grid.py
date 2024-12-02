class Solution:
    from heapq import heappush,heappop
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        pq=[(0,0,0)]
        visited=set()
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        while pq:
            curr,i,j=heappop(pq)
            
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i==rows-1 and j==cols-1:
                return curr
            for u,v in directions:
                x=u+i
                y=v+j
                if x in range(0,rows) and y in range(0,cols) and (x,y) not in visited:
                    if curr+1>=grid[x][y]:
                        heappush(pq,(curr+1,x,y))
                    else:
                        wait_time=grid[x][y]-curr
                        if wait_time%2==1:
                            next_time=curr+wait_time
                        else:
                            next_time=curr+wait_time+1
                        heappush(pq,(next_time,x,y))

        return -1