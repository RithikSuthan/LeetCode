class Solution:
    import copy
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        max_ls=[]
        my_dict1={}
        for i in range(len(nums)):
            if nums[i] not in my_dict1:
                my_dict1[nums[i]]=[]
            my_dict1[nums[i]].append(i)
        nums.sort()
        max_sum=float("-inf")
        for i in range(0,len(nums)-k+1):
            max_sum=max(sum(nums[i:k+i]),max_sum)
            max_ls=nums[i:k+i]
        result=["a" for i in range(len(nums))]
        print(result)
        print(my_dict1)
        print(max_ls)
        for i in max_ls:
            val=my_dict1[i].pop(0)
            result[val]=i
        ans=[]
        for i in range(len(result)):
            if result[i]!="a":
                ans.append(result[i])
        return ans