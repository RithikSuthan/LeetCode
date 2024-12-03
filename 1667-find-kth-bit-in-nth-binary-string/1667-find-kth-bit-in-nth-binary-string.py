class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(str1):
            temp=list(str1)
            # print("Before ",temp)
            for i in range(len(temp)):
                if temp[i]=="0":
                    temp[i]="1"
                else:
                    temp[i]="0"
            temp="".join(temp)
            # print(temp)
            return temp,temp[::-1]
        ans="0"
        for i in range(1,n):
            # print(i,ans)
            temp=ans[:]
            invert,reverse_=helper(temp)
            ans=ans+"1"+reverse_
        # print(ans)
        return ans[k-1]
