class Solution:
    import copy
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1 for i in range(len(nums))]
        for i in range(len(nums)):
            visit=False
            for j in range(i,len(nums)):
                # print(i," ",j," ",nums[j])
                if nums[i]<nums[j]:
                    ans[i]=nums[j]
                    visit=True
                    break
            if not visit:
                for k in range(0,i):
                    if nums[i]<nums[k]:
                        ans[i]=nums[k]
                        break
        print(ans)
        return ans
                