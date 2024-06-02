class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        l=len(nums)
        while(i<l-1):
            if nums[i]>nums[i+1]:
                break
            i=i+1
        if i+1==len(nums):
            return nums[0]
        print(i)
        return nums[i+1]
        