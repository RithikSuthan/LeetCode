from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        result = {}
        l = len(bloomDay)
        days = min(bloomDay) - 1
        
        if k * m > l:
            return -1
        if k * m == l:
            return max(bloomDay)

        def helper(day):
            bouq,flower=0,0
            for i in range(l):
                if bloomDay[i]<=day:
                    flower+=1
                else:
                    bouq+=flower//k
                    flower=0
            bouq+=flower//k
            if bouq>=m:
                return True
            return False
        min1,max1=min(bloomDay),max(bloomDay)
        while min1<max1:
            mid=(min1+max1)//2
            if helper(mid):
                max1=mid
            else:
                min1=mid+1
        return min1