class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backtrack(start,curr,target,curr_sum):
            if curr_sum==target and curr not in result:
                result.append(curr[:])
            elif target<curr_sum:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if curr_sum+candidates[i] > target:
                    break
                curr.append(candidates[i])
                backtrack(i+1,curr,target,curr_sum+candidates[i])
                curr.pop()
        backtrack(0,[],target,0)
        print(result)
        return result