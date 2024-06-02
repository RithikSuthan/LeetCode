class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls=nums1+nums2
        ls.sort()
        half=len(ls)//2
        if len(ls)%2==0:
            return (ls[half-1]+ls[half])/2
        return ls[half]