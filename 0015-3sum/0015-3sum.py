class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        k=0
        l=len(nums)-1
        ans=[]
        while(k<len(nums)):
            i=k+1
            j=l
            while(i<j):
                # print([nums[k],nums[i],nums[j]])
                if nums[k]+nums[i]+nums[j]==0:
                    if [nums[k],nums[i],nums[j]]  not in ans:
                        ans.append([nums[k],nums[i],nums[j]])
                    i=i+1
                    # break
                elif (nums[k]+nums[i]+nums[j])<0:
                    i=i+1
                else:
                    j=j-1
            k=k+1
        # print(ans)
        return ans