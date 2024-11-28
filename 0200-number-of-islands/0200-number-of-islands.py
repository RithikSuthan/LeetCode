class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(u,v):
            queue = deque()
            queue.append((u,v))

            while queue:
                curr = queue.popleft()
                visited.add(curr)
                for u,v in directions:
                    x = curr[0]+u
                    y = curr[1]+v
                    if x in range(0,rows) and y in range(0,cols) and grid[x][y]=="1" and (x,y) not in queue and (x,y) not in visited:
                        queue.append((x,y))


        
        rows = len(grid)
        cols = len(grid[0])
        noOfIslands = 0
        visited = set()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    noOfIslands += 1
        return noOfIslands
