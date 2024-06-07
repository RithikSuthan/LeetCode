class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag=False
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            elif flag:
                return False

            if i==0 or nums[i+1]>=nums[i-1]:
                nums[i]=nums[i+1]
            else:
                nums[i+1]=nums[i]
            flag=True
        return True