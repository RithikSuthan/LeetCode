class Solution(object):
    def smallestDistancePair(self, nums, k):
        def count_pair(mid):
            j,count=0,0
            for i in range(len(nums)):
                while (j<len(nums) and (nums[j]-nums[i])<=mid):
                    j+=1
                count+=j-i-1
            return count
        nums.sort()
        left=0
        right=nums[-1]
        while(left<right):
            mid=(left+right)//2
            if count_pair(mid)<k:
                left=mid+1
            else:
                right=mid
        return left
        