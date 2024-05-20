class Solution:
    import copy
    def myAtoi(self, s: str) -> int:
        temp=copy.deepcopy(s)
        str1=""
        neg=0
        i=0
        while(i<len(s)): #reach first number
            if s[i]>='A' and s[i]<='Z' or s[i]>='a' and s[i]<='z':
                return 0
            elif s[i]>='0' and s[i]<='9':
                break
            elif s[i]=='-' and neg==0 and i+1< len(s) and s[i+1]>='0' and s[i+1]<='9':
                neg=-1
            elif s[i]=="+" and neg==0 and i+1< len(s) and s[i+1]>='0' and s[i+1]<='9':
                neg=1
            elif s[i]==" ":
                pass
            else:
                return 0
            i=i+1
        s=s[i:]
        i=0
        while(i<len(s)):
            if s[i]>='0' and s[i]<='9':
                pass
            else:
                break
            i=i+1
        s=s[:i]
        if len(s)<1:
            return 0
        val=int(s)
        if neg==-1:
            val=-val
        if val>2**31-1:
            return 2**31-1
        elif val<-2**31:
            return -2**31
        return val