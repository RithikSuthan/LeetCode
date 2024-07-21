class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currsum=0
        left=0
        ans=float("inf")
        min_len=len(nums)
        for r in range(len(nums)):
            currsum+=nums[r]
            # print(left,r,"currsum = ",currsum)
            while(currsum>=target):
                currsum-=nums[left]
                ans=min(len(nums[left:r+1]),ans)
                left+=1    
        if ans==float("inf"):
            return 0
        return ans