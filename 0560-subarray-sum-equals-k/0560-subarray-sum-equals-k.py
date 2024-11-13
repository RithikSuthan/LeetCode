class Solution:
    from collections import defaultdict
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        mydict=defaultdict(int)
        mydict[0]=1  #[] can be a subarray when k is 0
        for i in range(0,len(nums)):
            # print(mydict,count)
            prefix+=nums[i]
            if (prefix-k) in mydict:
                count+=mydict[prefix-k]
            mydict[prefix]+=1
        return count
        