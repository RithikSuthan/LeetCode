class Solution(object):
    from collections import deque
    def pacificAtlantic(self, heights):
        rows=len(heights)
        cols=len(heights[0])
        directions=[[0,-1],[0,1],[1,0],[-1,0]]
        pacific=[]
        atlantic=[]
        pacific_soln=set()
        atlantic_soln=set()

        def bfs(starts,reachable):
            queue=deque(starts)
            visited=set(starts)
            while(queue):
                curr=queue.popleft()
                visited.add((curr[0],curr[1]))
                reachable.add((curr[0],curr[1]))
                for dire in directions:
                    u=curr[0]+dire[0]
                    v=curr[1]+dire[1]
                    if u in range(rows) and v in range(cols) and (u,v) not in visited:
                        if heights[curr[0]][curr[1]]<=heights[u][v]:
                            queue.append((u,v))        
        for i in range(cols):
            pacific.append((0,i))
            atlantic.append((rows-1,i))
        for i in range(rows):
            pacific.append((i,0))
            atlantic.append((i,cols-1))

        bfs(pacific,pacific_soln)
        bfs(atlantic,atlantic_soln)
        # print(pacific_soln," ",atlantic_soln)
        # print(result)
        result=list(pacific_soln & atlantic_soln)
        return result
