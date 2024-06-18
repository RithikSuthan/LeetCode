class Solution:
    from collections import defaultdict
    import bisect
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dict1=sorted(zip(difficulty,profit))
        l=len(worker)
        worker.sort()
        max_profit=0
        pos=0
        best=0
        for ele in worker:
            while pos<len(dict1) and ele>=dict1[pos][0]:
                best=max(best,dict1[pos][1])
                pos+=1
            max_profit+=best
        return max_profit
