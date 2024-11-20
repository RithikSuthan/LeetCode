class Solution:
    from collections import Counter
    def takeCharacters(self, s: str, k: int) -> int:
        total=Counter(s)
        if total['a']<k or total['b']<k or total['c']<k:
            return -1

        ans = float("inf")
        l=0
        for r in range(len(s)): 
            total[s[r]]-=1
            while total['a']<k or total['b']<k or total['c']<k:
                total[s[l]]+=1
                l+=1
            ans=min(ans,len(s)-(r-l+1))
        return ans