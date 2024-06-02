class Solution:
    import copy
    def search(self, nums: List[int], target: int) -> int:
        temp=copy.deepcopy(nums)
        nums.sort()
        l=0
        h=len(nums)
        while(l<h):
            m=(l+h)//2
            if nums[m]==target:
                return temp.index(nums[m])
            elif nums[m]>target:
                h=m
            else:
                l=m+1
        return -1