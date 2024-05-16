class Solution:
    def rob_house(self,nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        memo={1:nums[0],
              2:max(nums[0],nums[1])
             }
        for i in range(3,len(nums)+1):
                memo[i]=max(memo[i-1],memo[i-2]+nums[i-1])
        return memo[len(nums)]
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(self.rob_house(nums[0:len(nums)-1]),self.rob_house(nums[1:len(nums)]))            
            