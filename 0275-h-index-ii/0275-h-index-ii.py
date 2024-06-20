class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_citations=0
        def helper(target):
            nonlocal max_citations
            count=0
            for i in range(len(citations)):
                if citations[i]>=target:
                    count+=1
            print("Target",target,count)
            if count>=target:
                max_citations=max(max_citations,target)
                return True
            return False
        if len(citations)==1 and citations[0]>0:
            return 1
        citations.sort()
        left=0
        right=len(citations)
        while(left<=right):
            mid=(left+right)//2
            print(left,mid,right)
            if helper(mid):
                left=mid+1
            else:
                right=mid-1
        return right
