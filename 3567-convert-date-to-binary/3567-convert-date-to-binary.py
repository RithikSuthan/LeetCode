class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ls=date.split("-")
        ans=""
        for ele in ls:
            val=bin(int(ele))
            ans+=val[2:]+"-"
        ans=ans[:len(ans)-1]
        # print(ans)
        return ans