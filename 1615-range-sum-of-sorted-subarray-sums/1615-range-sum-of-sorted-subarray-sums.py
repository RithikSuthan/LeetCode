class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                ans.append(sum(nums[i:j+1]))
        ans.sort(key=lambda x:x)
        if not ans:
            return 0
        return sum(ans[left-1:right])%(10**9 +7)