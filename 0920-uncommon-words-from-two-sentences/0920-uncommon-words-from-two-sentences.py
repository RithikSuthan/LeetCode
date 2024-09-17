class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ls=list(s1.split(" "))
        ls2=list(s2.split(" "))
        ans=set()
        for ele in ls:
            if ls.count(ele)<=1 and ele not in ls2:
                ans.add(ele)
        for ele in ls2:
            if ls2.count(ele)<=1 and ele not in ls:
                ans.add(ele)
        # print(ans)  
        return list(ans)