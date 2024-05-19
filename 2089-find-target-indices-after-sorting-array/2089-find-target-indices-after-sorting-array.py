class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans=[]
        if target in nums:
            start=nums.index(target)
            while(target in nums[start:]):
                ans.append(start)
                start=start+1
            print(ans)
        return ans