from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        visited=set()
        queue=deque()
        newqueue=deque()
        time=0
        def bfs(queue):
            nonlocal newqueue
            newqueue=deque()
            while(queue):
                curr=queue.popleft()
                
                for i in directions:
                    u=curr[0]+i[0]
                    v=curr[1]+i[1]
                    # print(newqueue)
                    if u in range(rows) and v in range(cols) and grid[u][v]==1 and (u,v) not in visited:
                        newqueue.append((u,v))
                        visited.add((u,v))
                        grid[u][v]=2
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2 and (i,j) not in visited:
                    newqueue.append((i,j))
        while(newqueue):
            # print(time," ",newqueue," ",grid)
            bfs(newqueue)
            if not newqueue:
                break
            time=time+1        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1
        return time
