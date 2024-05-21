class Solution:
    import copy
    def subsetXORSum(self, nums: List[int]) -> int:
        result=[]
        def backtrack(start,curr):
            result.append(copy.deepcopy(curr))
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0,[])
        ans=0
        for i in range(len(result)):
            sum1=0
            for j in range(len(result[i])):
                sum1=bin(sum1)
                str1=bin(result[i][j])
                a=int(sum1[2:],2)
                b=int(str1[2:],2)
                sum1= a^b 
            ans=ans+sum1
        return ans