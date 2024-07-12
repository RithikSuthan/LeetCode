class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2!=0:
            return False
        # print("full ",target)
        target=sum(nums)//2
        # print("hslf",target)
        dp=set()
        dp.add(0)
        for i in range(0,len(nums),1):
            temp=set()
            for j in dp:
                temp.add(nums[i]+j)
                temp.add(j)
            dp=temp
            # print(dp)
            if target in dp:
                return True
        return False