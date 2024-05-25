class Solution(object):
    def permute(self, nums):
        result=[]
        def permutate(start):
            if start==len(nums):
                result.append(nums[:])
            for i in range(start,len(nums)):
                nums[i],nums[start]=nums[start],nums[i]
                permutate(start+1)
                nums[i],nums[start]=nums[start],nums[i]
        permutate(0)
        # print(result)
        return result