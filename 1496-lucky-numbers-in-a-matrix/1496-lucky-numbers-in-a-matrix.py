class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        ans=[]
        for i in range(m):
            val=min(matrix[i])
            ind=matrix[i].index(val)
            # print("main",i,val)
            cou=0
            flag=False
            for t in range(0,i,1):
                if matrix[t][ind]>=val:
                    flag=True
            for b in range(i+1,m,1):
                if matrix[b][ind]>=val:
                    flag=True
            if not flag:
                ans.append(val)
        return ans