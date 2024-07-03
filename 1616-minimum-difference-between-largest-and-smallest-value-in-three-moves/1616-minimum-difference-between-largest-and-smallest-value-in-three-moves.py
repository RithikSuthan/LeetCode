from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) <= 4:
            return 0
        print(nums)
        scenario1 = nums[-1] - nums[3]  
        scenario2 = nums[-2] - nums[2]  
        scenario3 = nums[-3] - nums[1]  
        scenario4 = nums[-4] - nums[0]      
        print(scenario1,scenario2,scenario3,scenario4)
        return min(scenario1, scenario2, scenario3, scenario4)

