class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ls=[]
        for i in nums:
            if i%2==0:
                ls.append(0)
            else:
                ls.append(1)
        dict1={}
        dict1[0]=1
        prev_sum=0
        for i in range(len(nums)):
            ls[i]=ls[i]+prev_sum
            prev_sum=ls[i]
        result=0
        for ele in ls:
            if ele-k in dict1:
                result+=dict1[ele-k]
            if ele in dict1:
                dict1[ele]+=1
            else:
                dict1[ele]=1
        return result