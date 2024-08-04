class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        st=[]
        str1=""
        i=0
        if s in t:
            return True
        if (not t and s )or (not s and t) :
            return False
        flag=True
        while flag and i<len(s):
            prev=t[:]
            val=t.find(s[i])
            if val==-1 or (st and st[-1]>val):
                t=list(t)
                t[val]='@'
                t=''.join(t)
            else:
                st.append(val)
                str1+=t[val]
                t=list(t)
                t[val]='@'
                t=''.join(t)
                i+=1
            if prev==t:
                return False
            # print(st,t)
        if s==str1:
            return True
        return False