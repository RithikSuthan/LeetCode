class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in set(nums1):
            j=0
            while(j<min(nums1.count(i),nums2.count(i))):
                ans.append(i)
                j=j+1
            
        # print(ans)
        
        return ans
            
            