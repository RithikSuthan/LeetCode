class Solution:
    import copy
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(start,curr):
            ls1=copy.deepcopy(curr)
            ls1.sort()
            if ls1 not in result:
                result.append(ls1)
            # print(result)
            for i in range(start,len(nums)):
                curr.append(nums[i])
                # print(curr)
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0,[])
        # print(result)    
        # result.sort()
        return result