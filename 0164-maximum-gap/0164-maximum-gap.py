class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        max_diff=0
        for i in range(len(nums)-1):
            if abs(nums[i+1]-nums[i])>max_diff:
                max_diff=abs(nums[i+1]-nums[i])
        print(max_diff)
        return max_diff