class Solution(object):
    import heapq
    def nthUglyNumber(self, n):
        heap=[]
        if (n<=0):
            return -1
        heappush(heap,1)
        seen=set()
        ugly_number=1
        ls=[2,3,5]
        for i in range(n):
            ugly_number=heappop(heap)
            for j in ls:
                new_ugli=j*ugly_number
                if new_ugli not in seen:
                    seen.add(new_ugli)
                    heappush(heap,new_ugli)
        return ugly_number