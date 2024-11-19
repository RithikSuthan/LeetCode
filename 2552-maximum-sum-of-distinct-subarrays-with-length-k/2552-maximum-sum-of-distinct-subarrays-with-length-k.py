class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window=set()
        curr_sum=0
        left=0
        max_sum=0
        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                curr_sum-=nums[left]
                left+=1
            window.add(nums[right])
            curr_sum+=nums[right]

            if right-left==k-1:
                max_sum=max(max_sum,curr_sum)
                window.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            
        return max_sum