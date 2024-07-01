class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_position=[]
        max_cou=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero_position.append(i)
        if len(zero_position)==0:
            return len(nums)-1
        for i in range(0,len(zero_position)):
            if i>0:
                start=zero_position[i-1]+1
            else:
                start=0
            cou=-1
            print(start)
            while( start<len(nums) ):
                # if nums[start]==0 and start<=zero_position[i]:
                    # continue
                if nums[start]==0 and start>zero_position[i]:
                    break
                start+=1
                cou+=1
            print(cou)
            max_cou=max(cou,max_cou)
        print(max_cou)
        return max_cou