class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float("-inf")
        max_end=0
        for i in range(len(nums)):
            max_end=max_end+nums[i]
            if max_sum<max_end:
                max_sum=max_end
            if max_end<0:
                max_end=0
        return max_sum