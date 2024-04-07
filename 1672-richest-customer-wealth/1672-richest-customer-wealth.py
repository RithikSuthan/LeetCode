class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max1=0
        for i in accounts:
            if max1<sum(i):
                max1=sum(i)
        return max1
        