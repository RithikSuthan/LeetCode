class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        memo={}
        def decode(index):
            if index in memo:
                return memo[index]
            if index==len(s):
                return 1
            if s[index]=="0":
                return 0
            count=decode(index+1)
            if index+1<len(s) and (s[index] == '1' or (s[index] == '2' and s[index + 1] in "0123456")):
                count+=decode(index+2) 
            memo[index]=count
            return memo[index]
        return decode(0)