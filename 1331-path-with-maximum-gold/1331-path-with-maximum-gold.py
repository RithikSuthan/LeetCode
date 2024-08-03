class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        def dfs(i,j,visited,curr_gold):
            nonlocal directions,grid
            curr_gold+=grid[i][j]
            max_gold=curr_gold
            visited.add((i,j))
            for ele in directions:
                u=i+ele[0]
                v=j+ele[1]
                if u in range(0,len(grid)) and v in range(0,len(grid[0])) and (u,v) not in visited  and grid[u][v]!=0:                       
                    max_gold=max(max_gold,dfs(u,v,visited,curr_gold))
            visited.remove((i,j))
            curr_gold-=grid[i][j]
            return max_gold
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    ans=max(ans,dfs(i,j,set(),0))
                    print(ans)
        return ans