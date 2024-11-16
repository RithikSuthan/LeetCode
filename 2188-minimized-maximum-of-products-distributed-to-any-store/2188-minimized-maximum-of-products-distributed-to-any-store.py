class Solution:
    import math
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(val):
            temp=0
            for ele in quantities:
                temp+=ceil(ele/val)
            print(val,temp)
            return temp<=n
        l=1
        h=max(quantities)
        while(l<h):
            mid=(l+h)//2
            if canDistribute(mid):
                h=mid
            else:
                l=mid+1
        return l
            