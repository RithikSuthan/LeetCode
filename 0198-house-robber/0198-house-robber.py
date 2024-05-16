class Solution:
    def house(self,nums,memo,n):
        if n<=0:
            return 0
        if n not in memo:
            print(n,memo[n-1],memo[n-2]+nums[n-1])
            memo[n]=max(memo[n-1],memo[n-2]+nums[n-1])
        return memo[n]
    def rob(self, nums: List[int]) -> int:
        if len(nums)>1:
            memo={1:nums[0],2:max(nums[0],nums[1])}
        elif len(nums)==0:
            return 0
        else:
            return nums[0]
        for i in range(3,len(nums)+1):
            memo[i]=self.house(nums,memo,i)
        print(memo)
        return memo[len(nums)]