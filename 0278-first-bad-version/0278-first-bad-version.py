# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=0
        right=n
        mid=0
        first=n
        while(left<=right):
            mid=(left+right)//2
            print(left,mid,right)
            result=isBadVersion(mid)
            if result==True:
                first=min(mid,first)
            if result==False:
                left=mid+1
            else:
                right=mid-1
        return first