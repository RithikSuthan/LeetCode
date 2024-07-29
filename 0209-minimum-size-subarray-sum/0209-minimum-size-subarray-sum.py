class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum=0
        left=0
        right=0
        min_len=float("inf")
        while(right<len(nums)):
            currSum+=nums[right]
            while(currSum>=target):
                min_len=min(min_len, right-left+1 )
                currSum-=nums[left]
                left+=1
            right+=1
        if min_len==float("inf"):
            return 0
        return min_len