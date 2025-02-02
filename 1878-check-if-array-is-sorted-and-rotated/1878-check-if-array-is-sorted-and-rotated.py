class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = nums[:]
        temp.sort()
        for i in range(0,len(temp)):
            nums.insert(0,nums.pop())
            if( nums == temp  ):
                return True
        return False