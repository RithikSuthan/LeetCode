class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ls=[]
        ltr=[]
        for i in range(len(s)):
            if ((s[i]>='a' and s[i]<='z') or s[i]>='A' and s[i]<='Z'):
                ltr.append(s[i])
            else:
                ls.append([i,s[i]])
        ltr=ltr[::-1]
        # ans="".join(ltr)
        for ele in ls:
            ltr.insert(ele[0],ele[1])
        ans="".join(ltr)
        # print(ans)
        # print(ltr,ls)
        return ans