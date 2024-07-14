class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opr=0
        for i in nums:
            if i%3!=0:
                opr+=1
        return opr