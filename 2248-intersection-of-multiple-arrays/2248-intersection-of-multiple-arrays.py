class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        len1=len(nums)
        if len1<=1:
            nums[0].sort()
            return nums[0]
        for i in set(nums[0]):
            min1=float("inf")
            for j in range(1,len1):
                min1=min(min1,nums[j].count(i))
            if min1!=float("inf"):
                for k in range(min1):
                    ans.append(i)
        ans.sort()
        return ans
                