class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls=set(nums1).intersection(set(nums2))
        ans=[]
        for  i in ls:
            j=0
            while j<min(nums1.count(i),nums2.count(i)):
                ans.append(i)
                j+=1 
        return ans
