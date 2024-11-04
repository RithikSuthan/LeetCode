class Solution:
    from collections import defaultdict
    def compressedString(self, word: str) -> str: 
        ls=[]
        i=0
        curr=""
        while(i<len(word)):
            if  curr!="" and curr[-1]!=word[i]:
                ls.append(curr)
                curr=""
            curr+=word[i]
            i+=1
        ls.append(curr)
        print(ls)

        ans=""
        for ele in ls:
            cou=ele.count(ele[0])
            while(cou>=9):
                ans+="9"+ele[0]
                cou-=9
            if cou>0:
                ans+=str(cou)+ele[0]
            # print(ans)
        return ans