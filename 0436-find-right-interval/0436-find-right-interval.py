class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        indexed_interval=[(intervals[i][0],i) for i in range(len(intervals))]
        indexed_interval.sort()
        def bin_search(target):
            left=0
            right=len(indexed_interval)-1
            while(left<right):
                mid=(left+right)//2
                if indexed_interval[mid][0]<target:
                    left=mid+1
                else:
                    right=mid
            return left
        result=[]
        for interval in intervals:
            target=interval[1]
            ind=bin_search(target)
            if ind<len(intervals) and indexed_interval[ind][0]>=target:
                result.append(indexed_interval[ind][1])
            else:
                result.append(-1)
        return result