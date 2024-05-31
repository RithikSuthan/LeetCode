class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binSearch(l,u):
            mid=(l+u)//2
            if(l>u):
                return -1
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                return binSearch(mid+1,u)
            elif nums[mid]>target:
                return  binSearch(l,mid-1)
        result=binSearch(0,len(nums)-1)
        # print(result)
        return result