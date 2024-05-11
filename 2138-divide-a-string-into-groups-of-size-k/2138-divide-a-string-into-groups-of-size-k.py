class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans=[]
        for i in range(0,len(s),k):
            temp=s[i:i+k]
            if len(temp)==k:
                ans.append(temp)
            else:
                while(len(temp)!=k):
                    temp=temp+fill
                ans.append(temp)
        # print(ans)
        return ans