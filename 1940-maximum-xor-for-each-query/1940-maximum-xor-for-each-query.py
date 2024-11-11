class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val=2**maximumBit-1
        print(max_val)

        total_xor=[nums[0]]
        for i in range(1,len(nums)):
            total_xor.append(total_xor[-1]^nums[i])
        total_xor=total_xor[::-1]
        print(total_xor)
        ans=[]
        for i in range(0,len(nums)):
            ans.append(max_val^total_xor[i])
        return ans
