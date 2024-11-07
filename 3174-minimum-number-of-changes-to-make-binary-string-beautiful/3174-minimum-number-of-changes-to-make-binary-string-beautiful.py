class Solution:
    def minChanges(self, s: str) -> int:
        l=len(s)
        change=0
        temp=[]
        for i in range(0,l,2):
            temp.append(s[i:i+2])
        for ele in temp:
            if ele.count("0")==1:
                change+=1        
        return change