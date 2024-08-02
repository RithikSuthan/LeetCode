class Solution:
    from collections import defaultdict
    def minSwaps(self, nums: List[int]) -> int:
        cou=nums.count(1)
        curr=[nums[i] for i in range(cou)]
        curr=sum(curr)
        ans=curr
        for i in range(1,len(nums)):
            curr-=nums[i-1]
            curr+=nums[(i+cou-1)%len(nums)]
            ans=max(ans,curr)
        return cou-ans