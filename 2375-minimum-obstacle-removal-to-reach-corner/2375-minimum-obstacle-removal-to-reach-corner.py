class Solution:
    from heapq import heappush,heappop
    def minimumObstacles(self, grid: List[List[int]]) -> int:
                
        rows = len(grid)
        cols = len(grid[0])

        if rows==1:
            return grid[0].count(1)
        elif cols==1:
            temp = 0
            for ele in grid:
                if ele[0]==1:
                    temp+=1
            return temp

        pq=[(0,0,0)]
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        min_obstacle = [[float('inf')] * cols for _ in range(rows)]
        min_obstacle[0][0]=0
        while pq:
            curr_obstacles,i,j=heappop(pq)
            for u,v in directions:
                x = i+u
                y = j+v
                if x == rows-1 and y == cols-1:
                    return curr_obstacles
                if x in range(0,rows) and y in range(0,cols):
                    new_obstacle=curr_obstacles+(1 if grid[x][y]==1 else 0)

                    if new_obstacle < min_obstacle[x][y]:
                        min_obstacle[x][y]=new_obstacle
                        heappush(pq,(new_obstacle,x,y))

        return min_obstacle[rows-1][cols-1]

