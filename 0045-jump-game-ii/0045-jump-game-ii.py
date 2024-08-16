class Solution:
    from collections import defaultdict
    def jump(self, nums: List[int]) -> int:
        memo=defaultdict(int)
        def helper(ind):
            nonlocal memo
            if ind in memo:
                return memo[ind]
            if ind==len(nums)-1:
                return 0
            if ind>=len(nums):
                return float("inf")
            memo[ind] = float('inf')
            for i in range(1,nums[ind]+1):
                memo[ind]=min(memo[ind],1+helper(ind+i))
            return memo[ind]
        helper(0)
        print(memo)
        return memo[0]
