class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2.sort()
        ans=[-1 for i in range(len(nums1))]
        
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums1[i]<nums2[j]:
                    ans[i]=nums2[j]
                    break
        print(ans)
        return ans