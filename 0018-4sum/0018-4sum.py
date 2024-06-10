class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        l=len(nums)
        nums.sort(key=lambda x:x)
        print(nums)
        i=0
        while(i<l-3):
            j=i+1
            while(j<l-2):
                k=j+1
                m=l-1
                while(k<m):
                    val=nums[i]+nums[j]+nums[k]+nums[m]
                    if val==target and [nums[i],nums[j],nums[k],nums[m]] not in result:
                        result.append([nums[i],nums[j],nums[k],nums[m]])
                    elif val>target:
                        m=m-1
                    else:
                        k=k+1 
                j+=1
            i+=1
        print(result)
        return result
        
    