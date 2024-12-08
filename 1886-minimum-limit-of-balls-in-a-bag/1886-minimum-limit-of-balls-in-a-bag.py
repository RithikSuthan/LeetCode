class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def oprCount(val):
            temp = 0
            for i in range(len(nums)):
                temp += ceil(nums[i] / val ) -1
            return temp
        minBall = 1
        maxBall = max(nums)
        while(minBall < maxBall):
            mid = (minBall + maxBall)//2
            if ( oprCount(mid) <= maxOperations ) :
                maxBall = mid 
            else : 
                minBall = mid + 1
        return maxBall        
