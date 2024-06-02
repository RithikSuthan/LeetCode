class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatBanana(piles,k):
            t=0
            for i in piles:
                t+=ceil(i/k)
            # print("t=",t)
            return t
        l=1
        h1=max(piles)
        while(l<h1):
            # print(l," ",h1)
            mid=(l+h1)//2
            if canEatBanana(piles,mid) > h:
                l=mid+1
            else:
                h1=mid
        return l