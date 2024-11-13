class Solution:
    import bisect
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count=0
        for i in range(0,len(nums)):
            left=bisect.bisect_left(nums,lower-nums[i],i+1)
            right=bisect.bisect_right(nums,upper-nums[i],i+1)-1
            if left<=right:
                count+=right-left+1
        return count