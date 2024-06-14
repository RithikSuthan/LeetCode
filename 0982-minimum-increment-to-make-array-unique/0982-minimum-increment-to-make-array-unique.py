class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x)
        cou=0
        for i in range(1,len(nums)):
            if(nums[i])<=nums[i-1]:
                bal=nums[i-1]-nums[i]+1
                nums[i]=nums[i]+bal
                cou+=bal
        return cou   
