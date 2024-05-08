class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums=list(set(nums))
        nums.sort()
        len_max=1
        i=0
        cou=1
        while(i<len(nums)-1):
            # print(nums[i]," ",nums[i+1])
            if nums[i]==nums[i+1]-1:
                cou=cou+1
            else:
                cou=1
            len_max=max(len_max,cou)
            i=i+1
        print(len_max)
        return len_max