class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1=defaultdict()
        for i in range(len(nums)):
            diff=target-nums[i]
            # print(nums[i],diff)
            if diff in dict1:
                return [i,dict1[diff]]
            dict1[nums[i]]=i
            # print(dict1)
        return [-1,-1]