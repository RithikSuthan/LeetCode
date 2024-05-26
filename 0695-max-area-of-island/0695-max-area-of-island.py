class Solution(object):
    from collections import deque
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area=0
        visited=set()
        rows=len(grid)
        cols=len(grid[0])
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(i,j):
            nonlocal max_area
            queue=deque()
            queue.append((i,j))
            area=1
            while(queue):
                curr=queue.popleft()
                visited.add(curr)
                for i in directions:
                    u=curr[0]+i[0]
                    v=curr[1]+i[1]
                    if u>=0 and u<rows and v>=0 and v<cols and (u,v) not in visited and grid[u][v]==1 and (u,v) not in queue:
                        queue.append((u,v))
                        area=area+1
                    print(queue)
            print(area)
            max_area=max(max_area,area)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    dfs(i,j)            
        return max_area