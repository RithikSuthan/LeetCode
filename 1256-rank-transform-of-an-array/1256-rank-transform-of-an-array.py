class Solution:
    from collections import defaultdict
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        temp=arr[:]
        temp.sort()
        rank=defaultdict()
        curr_rank=1
        for i in range(len(temp)):
            if temp[i] not in rank:
                rank[temp[i]]=curr_rank
                curr_rank+=1
        for i in range(len(arr)):
            arr[i]=rank[arr[i]]
        return arr