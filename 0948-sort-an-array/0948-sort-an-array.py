from collections import defaultdict
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=partition(nums[0:mid])
            right=partition(nums[mid:])
            return merge(left,right)
        def merge(left,right):
            i=0
            j=0
            ans=[]
            while(i<len(left) and j<len(right)):
                if left[i]<right[j]:
                    ans.append(left[i])
                    i+=1
                else:
                    ans.append(right[j])
                    j+=1
            ans.extend(left[i:])
            ans.extend(right[j:])
            # print(ans)
            return ans
        return partition(nums)
            