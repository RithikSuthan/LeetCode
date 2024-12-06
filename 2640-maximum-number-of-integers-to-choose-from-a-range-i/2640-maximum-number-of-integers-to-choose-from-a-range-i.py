class Solution:
    import bisect
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        ind=bisect.bisect_right(banned,n)
        st=set(banned[:ind])
        prefix=0
        cou=0
        for i in range(1,n+1):
            if i not in st:
                if prefix+i<=maxSum:
                    prefix+=i
                    cou+=1
                else:
                    break
        return cou

        return 0