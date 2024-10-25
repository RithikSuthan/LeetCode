class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans=0
        for ele in s:
            ans+=abs(s.index(ele)-t.index(ele))
        return ans