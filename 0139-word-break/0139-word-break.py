class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False  for i in range(0,len(s)+1)]
        dp[-1]=True
        for i in range(len(s)-1,-1,-1):
            print(i)
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                    if dp[i]:
                        break
            print(dp)

        return dp[0]