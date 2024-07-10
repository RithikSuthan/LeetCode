class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        ls=[[0 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]='A'
                    ls[i][j]='A'
        if ls[0][0]!='A':
            ls[0][0]=1
        for i in range(rows):
            for j in range(cols):
                if i>0 and ls[i][j]!='A' and ls[i-1][j]!='A':
                    ls[i][j]+=ls[i-1][j]
                if j>0 and ls[i][j]!='A' and ls[i][j-1]!='A':
                    ls[i][j]+=ls[i][j-1]
        print(ls)
        if ls[rows-1][cols-1]=='A':
            return 0
        elif rows==1 and cols==1:
            return 1
        return ls[rows-1][cols-1]
                
