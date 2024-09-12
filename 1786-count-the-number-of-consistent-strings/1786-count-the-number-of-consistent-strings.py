class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=0
        for ele in words:
            val=set(ele)
            flag=True
            for ele1 in val:
                if ele1 not in allowed:
                    flag=False
            if flag:
                ans+=1
        return ans