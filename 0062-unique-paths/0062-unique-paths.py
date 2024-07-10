class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ls=[[0 for i in range(n)] for j in range(m)]
        print(ls)
        ls[0][0]=1
        for i in range(0,m,1):
            for j in range(0,n,1):
                if i>0:
                    ls[i][j]+=ls[i-1][j]
                if j>0:
                    ls[i][j]+=ls[i][j-1]
        # print(ls)
        return ls[m-1][n-1]
