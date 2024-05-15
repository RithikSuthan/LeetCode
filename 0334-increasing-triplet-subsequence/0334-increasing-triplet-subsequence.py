class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3 or len(set(nums))<3:
            return False
        for i in range(len(nums)):
            result=[]
            result.append(nums[i])
            for j in range(i,len(nums)):
                if result[-1]<nums[j]:
                    result.append(nums[j])
                elif len(result)>1 and result[-2]<nums[j]:
                    result.pop()
                    result.append(nums[j])

                if len(result)>2:
                    return True
            print(result)
        return False