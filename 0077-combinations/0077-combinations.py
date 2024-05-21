class Solution:
    import copy
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        nums=[i for i in range(1,n+1)]
        def backtrack(start,curr):
            if len(curr)==k:
                result.append(copy.deepcopy(curr))
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0,[])
        return result