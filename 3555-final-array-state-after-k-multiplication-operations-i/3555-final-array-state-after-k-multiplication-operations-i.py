class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(0,k):
            min_ind=nums.index(min(nums))
            nums[min_ind]*=multiplier
        return nums
