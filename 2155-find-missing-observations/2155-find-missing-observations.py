class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        bal=mean*(len(rolls)+n)-sum(rolls)
        ls=[0 for i in range(n)]
        start=0
        while(bal!=0):
            ls[start]+=1
            if ls[start]>6:
                return []
            bal-=1
            start+=1
            if start>=len(ls):
                start=0
        # print(bal)
        # print(ls)
        if ls.count(0)>1:
            return []
        return ls