class Solution:
    import copy
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ls=copy.deepcopy(score)
        rank=["" for i in range(len(score))]
        i=1
        while(len(ls)!=0):
            ind=score.index(ls.pop( ls.index( max(ls)  ) ))
            if i==1:
                rank[ind]="Gold Medal"
            elif i==2:
                rank[ind]="Silver Medal"
            elif i==3:
                rank[ind]="Bronze Medal"
            else:
                rank[ind]=str(i)
            i=i+1
        # print(rank)
        return rank