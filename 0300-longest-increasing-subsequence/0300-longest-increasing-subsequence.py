class Solution:
    from collections import defaultdict
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo=defaultdict()  #dp top down approach
        # def dfs(index,last_value):
        #     nonlocal memo
        #     if index==len(nums):
        #         return 0
        #     if (index,last_value) in memo:
        #         return memo[(index,last_value)]
        #     exclude=dfs(index+1,last_value)
        #     include=0
        #     if nums[index]>last_value:
        #         include=1+dfs(index+1,nums[index])
        #     memo[(index,last_value)]=max(exclude,include)
        #     return memo[(index,last_value)]
        # return dfs(0,float("-inf"))
        dp=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)

            
