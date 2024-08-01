class Solution:
    from collections import defaultdict
    def rob(self, nums: List[int]) -> int:
        memo=defaultdict()
        def helper_func(i):
            nonlocal memo
            if i>=len(nums):
                return 0
            nonlocal memo
            if i in memo:
                return memo[i]
            memo[i]=max( nums[i]+ helper_func(i+2) ,
             helper_func(i+1) )
            return memo[i]
        helper_func(0)
        return memo[0]
            