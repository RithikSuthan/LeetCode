class Solution:
    from collections import defaultdict
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo=defaultdict()
        def helper(i,end):
            nonlocal memo
            if i>=end:
                return 0
            if i in memo:
                return memo[i]
            memo[i]=max( nums[i]+helper(i+2,end),helper(i+1,end) )
            return memo[i]
        left=helper(0,len(nums)-1)
        memo=defaultdict()
        right=helper(1,len(nums))
        return max( left,right )