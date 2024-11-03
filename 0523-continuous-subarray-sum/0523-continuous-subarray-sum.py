class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # ls=[]
        # right=0
        # while(right<len(nums)):
        #     left=0
        #     while(left<len(nums)):
        #         # print(nums[left:left+right+1])
        #         if sum(nums[left:left+right+1])%k==0 and len(nums[left:left+right+1])>=2:
        #             return True
        #         left+=1
        #     right+=1
        # return False
        cumm=0
        dict1={0:-1}
        for i in range(0,len(nums)):
            cumm+=nums[i]
            rem=cumm%k
            # print(dict1,cumm,i,rem)
            if rem in dict1 and i-dict1[rem]>=2:
                return True
            if rem not in dict1:
                dict1[rem]=i
        return False

