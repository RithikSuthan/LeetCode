class Solution:
    def minChanges(self, s: str) -> int:
        l=len(s)
        change=0
        mid=l//2
        l1=s[0:mid]
        l2=s[mid:]
        temp=[]
        for i in range(0,len(s),2):
            temp.append(s[i:i+2])
        for ele in temp:
            if ele.count("0")==1:
                change+=1        
        return change