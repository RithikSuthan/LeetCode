class Solution:
    def minimumDeletions(self, s: str) -> int:
        min1=float("inf")
        lsa=[]
        lsb=[]
        la=0
        lb=0
        for i in range(len(s)):
            lsb.append(lb)
            if s[i]=='b':
                lb+=1
        for k in range(len(s)-1,-1,-1):
            lsa.append(la)
            if s[k]=='a':
                la+=1
        lsa=lsa[::-1]
        # print(lsb)
        # print(lsa)
        for i in range(len(lsa)):
            print(abs( lsb[i]-lsa[i] ))
            min1=min( lsb[i]+lsa[i] ,min1)
        return min1