class Solution:
    def minChanges(self, s: str) -> int:
        l=len(s)
        if s.count("0")==l or s.count("1")==l:
            return 0
        
        # if len(s[0:l//2])%2!=0:
        #     return min(s.count("0"),s.count("1"))
        
        change=0
        mid=l//2
        l1=s[0:mid]
        l2=s[mid:]
        temp=[]
        for i in range(0,len(s),2):
            temp.append(s[i:i+2])
        print(temp)
        for ele in temp:
            if ele.count("0")==1:
                change+=1        
        return change