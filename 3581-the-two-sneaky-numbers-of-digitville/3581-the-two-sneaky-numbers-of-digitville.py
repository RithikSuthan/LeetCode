class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans=set()
        for i in range(0,len(nums)):
            if nums.count(nums[i])>1:
                ans.add(nums[i])
        return list(ans)